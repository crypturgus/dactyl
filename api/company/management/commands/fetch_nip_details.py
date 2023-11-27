import asyncio
import os

from django.core.management.base import BaseCommand

from company.company_data_fetcher import CompanyDataFetcher


class Command(BaseCommand):
    help = "Fetch data for a given NIP"

    def add_arguments(self, parser):
        parser.add_argument("nip", type=str, help="NIP number to fetch data for")

    def handle(self, *args, **options):
        nip_number = options["nip"]
        self.stdout.write(
            self.style.SUCCESS(f"Started fetching data for NIP {nip_number}")
        )

        company_data_fetcher = CompanyDataFetcher(
            browser_ws_endpoint=os.environ["BROWSER_URL"]
        )

        async def main():
            firstname = await company_data_fetcher.fetch_data_for_nip(nip_number)
            self.stdout.write(f"First name for NIP {nip_number}: {firstname}")

        asyncio.get_event_loop().run_until_complete(main())

        self.stdout.write(self.style.SUCCESS("Done"))
