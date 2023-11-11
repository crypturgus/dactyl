# import asyncio
#
# import pyppeteer
# from django.core.management.base import BaseCommand
#
#
# class Command(BaseCommand):
#     help = "Create a superuser"
#
#     def handle(self, *args, **kwargs):
#         self.stdout.write(
#             self.style.SUCCESS("Started fetching data for NIP 6141548074")
#         )
#
#         async def main():
#             browser = await pyppeteer.connect(
#                 options={"browserWSEndpoint": "ws://browserless:3000"}
#             )
#             page = await browser.newPage()
#             await page.goto(
#                 "https://aplikacja.ceidg.gov.pl/ceidg/ceidg.public.ui/search.aspx"
#             )
#
#             await page.type("#MainContentForm_txtNip", "6141548074")
#             await page.click('[name="ctl00$MainContentForm$btnInputSearch"]')
#             await asyncio.sleep(1)
#             await page.click("#MainContentForm_DataListEntities_hrefDetails_0")
#             await asyncio.sleep(1)
#             element = await page.querySelector("#MainContentForm_lblFirstName")
#             firstname = await page.evaluate("(element) => element.textContent", element)
#
#             print(firstname)
#
#             await page.screenshot({"path": "example.png"})
#
#             await browser.close()
#
#         asyncio.get_event_loop().run_until_complete(main())
#
#         self.stdout.write(self.style.SUCCESS("Done"))
