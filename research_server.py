import arxiv
import json
import os
from typing import List
from mcp.server.fastmcp import FastMCP
# import anthropic
# from dotenv import load_dotenv
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PAPER_DIR = "papers"

# Initialize the FASTMCP server
mcp = FastMCP("research")

@mcp.tool()
def search_papers(topic: str, max_results: int = 5) -> List[str]:
    '''
    Search for papers on arXiv based on a topic and store their information

    Args:
        topic: The topic to search for
        max_results: Maximum number of results to return

    Returns:
        List of paper IDs found in the search
    '''

    # Use arxiv to find the papers
    arxiv_client = arxiv.Client()

    # search for the most relavant articles matching the required topic
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = arxiv_client.results(search)
    # logger.info(f"Found {len(list(papers))} papers for topic '{topic}'")

    # Create directory for the topic
    path = os.path.join(PAPER_DIR, topic.lower().replace(" ", "_"))
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, "papers_info.json")

    # Try to load existing papers info
    try:
        with open(file_path, 'r') as json_file:
            papers_info = json.load(json_file)
    except(FileNotFoundError, json.JSONDecodeError):
        papers_info = {}

    # Process each paper and add to papers_info
    papers_ids = []
    for paper in papers:
        paper_id = paper.get_short_id()
        papers_ids.append(paper_id)
        paper_info = {
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "summary": paper.summary,
            "pdf_url": paper.pdf_url,
            "published": str(paper.published.date()),
        }

        papers_info[paper_id] = paper_info

    # Save the updated papers info to the file
    with open(file_path, 'w') as json_file:
        json.dump(papers_info, json_file, indent=4)
    
    logger.info(f"Papers search results on topic {topic} are saved in: {file_path}")
    return papers_ids

@mcp.tool()
def extract_info(paper_id: str) -> str:
    '''
    Search for information about a specific paper across all topic directories.
    
    Args:
        paper_id: The ID of the paper to look for
        
    Returns:
        JSON string with paper information if found, error message if not found
    '''

    for topic in os.listdir(PAPER_DIR):
        topic_path = os.path.join(PAPER_DIR, topic)
        
        if not os.path.isdir(topic_path):
            continue

        topic_papers_info_path = os.path.join(topic_path, "papers_info.json")
        if not os.path.isfile(topic_papers_info_path):
            continue

        try:
            with open(topic_papers_info_path, 'r') as json_file:
                papers_info = json.load(json_file)
                if paper_id in papers_info:
                    paper_info = papers_info[paper_id]
                    return json.dumps(paper_info, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            continue

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')