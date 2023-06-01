from py2neo import Graph


class Database(object):
    def __init__(self, uri="bolt://172.16.20.147:7687", user="neo4j", password="secret"):
        self.graph = Graph(uri, auth=(user, password))

    # def __del__(self):
    #     self._driver.close()
    #     print("Driver has been closed.")

    def query(self, query):
        """
        Return:
            result of the query, one record per iteration
        """
        res = self.graph.run(query)
        return res


if __name__ == "__main__":
    # test connection
    driver = Database()
    result = driver.query("match (n) return n limit 10")
    for i in result:
        print(i)
