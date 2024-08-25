from scrappers.categories import getCategoryList
import json

def main():
    categories = getCategoryList()
    print(json.dumps(categories, indent=4))
main()