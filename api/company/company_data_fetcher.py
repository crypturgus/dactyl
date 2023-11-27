import asyncio

import pyppeteer


class CompanyDataFetcher:
    def __init__(self, browser_ws_endpoint):
        self.browser_ws_endpoint = browser_ws_endpoint

    async def fetch_data_for_nip(self, nip_number):
        browser = await pyppeteer.connect(
            options={"browserWSEndpoint": self.browser_ws_endpoint}
        )
        page = await browser.newPage()
        await page.goto(
            "https://aplikacja.ceidg.gov.pl/ceidg/ceidg.public.ui/search.aspx"
        )

        # Perform the search
        await page.type("#MainContentForm_txtNip", nip_number)
        await page.click('[name="ctl00$MainContentForm$btnInputSearch"]')
        # TODO: Replace the sleep with a more reliable waiting method
        await asyncio.sleep(1)
        await page.click("#MainContentForm_DataListEntities_hrefDetails_0")
        await asyncio.sleep(1)  # TODO: As above

        # Extract data
        element = await page.querySelector("#MainContentForm_lblFirstName")
        firstname = await page.evaluate("(element) => element.textContent", element)

        # Optionally save a screenshot
        await page.screenshot({"path": "example.png"})

        # Close the browser
        await browser.close()

        # Return data
        return firstname
