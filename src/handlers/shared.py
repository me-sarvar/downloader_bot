from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=5)
SEARCH_RESULTS = {}