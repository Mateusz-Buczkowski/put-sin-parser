from selenium import webdriver


class Parser:
    def __init__(self, base_url="https://sin.put.poznan.pl/publications/details/"):
        self.base_url = base_url

    def get_single_publication_detail(self, paper_id="i17973"):
        with webdriver.Firefox() as driver:
            driver.get(f"{self.base_url}{paper_id}")

            data = dict()
            data['title'] = driver.find_element_by_name("citation_title").get_attribute("content")

            authors = driver.find_elements_by_name("citation_author")
            data['author'] = [author.get_attribute("content") for author in authors]

            return data


if __name__ == "__main__":
    parser = Parser()
    output = parser.get_single_publication_detail()
    print(output)
