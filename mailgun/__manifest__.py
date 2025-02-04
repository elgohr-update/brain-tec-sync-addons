# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Mailgun""",
    "summary": """Setup the outgoing and incoming mail flow easily by using Mailgun""",
    "category": "Discuss",
    # "live_test_url": "http://apps.it-projects.info/shop/product/mailgun?version=11.0",
    "images": ["images/mailgun_main.png"],
    "version": "13.0.1.1.0",
    "application": False,
    "author": "IT-Projects LLC, Ildar Nasyrov",
    "support": "apps@itpp.dev",
    "website": "https://itpp.dev",
    "license": "Other OSI approved licence",  # MIT
    "price": 195.00,
    "currency": "EUR",
    "depends": ["mail"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["data/ir_cron_data.xml"],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
    "demo_title": "Mailgun",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "mailgun",
    "demo_summary": "Easy to send outgoing and fetch incoming messages by using Mailgun",
    "demo_images": ["images/mailgun_main.png"],
}
