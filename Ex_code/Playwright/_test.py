from playwright.sync_api import Page, expect

def test_recherche_wikipedia(page: Page):
    page.goto("https://fr.wikipedia.org")

    expect(page.get_by_role("searchbox", name="Rechercher sur Wikipédia")).to_be_visible()
    expect(page.get_by_role("button", name="Rechercher")).to_be_visible()

    page.get_by_role("searchbox", name="Rechercher sur Wikipédia").click()
    page.get_by_role("searchbox", name="Rechercher sur Wikipédia").fill("Python")

    page.get_by_role("button", name="Rechercher").click()

    expect(page.locator("#firstHeading")).to_contain_text("Python")