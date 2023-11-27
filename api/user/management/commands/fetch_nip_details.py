import asyncio
import os

from django.core.management.base import BaseCommand

from company.company_data_fetcher import CompanyDataFetcher


class Command(BaseCommand):
    help = "Create a superuser"

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS("Started fetching data for NIP 6141548074")
        )

        # TODO: Move browser api endpoint to env var
        company_data_fetcher = CompanyDataFetcher(
            browser_ws_endpoint=os.environ["BROWSER_URL"]
        )
        # TODO: Make NIP number to be obtained as command arg
        nip_number = "6141548074"

        async def main():
            firstname = await company_data_fetcher.fetch_data_for_nip(nip_number)
            self.stdout.write(f"First name for NIP {nip_number}: {firstname}")

        asyncio.get_event_loop().run_until_complete(main())

        self.stdout.write(self.style.SUCCESS("Done"))
