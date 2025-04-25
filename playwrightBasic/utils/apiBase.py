from http.client import responses

from playwright.sync_api import Playwright
from pycparser.ply.yacc import token

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                             data={"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"authorization":token,
                                                     "content-type": "application/json"})
        print(response.json())
        responseBody = response.json()
        orderId = responseBody["orders"][0]
        return  orderId
