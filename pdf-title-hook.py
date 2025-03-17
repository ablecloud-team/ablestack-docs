from mkdocs.config.defaults import MkDocsConfig, Page
from mkdocs.structure.files import Files
from mkdocs.plugins import event_priority
import re

@event_priority(100)
def on_page_markdown(markdown: str,
                     page: Page,
                     config: MkDocsConfig,
                     files: Files):
    """
    The `page_markdown` event is called after the page's markdown is loaded
    from file and can be used to alter the Markdown source text. The meta-
    data has been stripped off and is available as `page.meta` at this point.

    Note:
        @event_priority(100) indicates that this should be first of the
        on_page_markdown events executed. This is important because
        mkdocs-exporter also uses @event_priority(100) for this event
        to add the cover pages. This event_priority allows us to add
        a h1 heading to the top of the page, but after the front cover page.

    Args:
        markdown: Markdown source text of page as string
        page: `mkdocs.structure.pages.Page` instance
        config: global configuration object
        files: global files collection

    Returns:
        Markdown source text of page as string
    """
    page_heading = f"# {page.title}\n\n"
    # Standard h1 markdown syntax (i.e., '# Title Text')
    H1_RE = re.compile(r"^\s*#\s+.+", re.MULTILINE)
    # Secondary h1 markdown syntax (text followed by a line of only '=')
    H1_RE_2 = re.compile(r"^.*\S.*\n\s{0,3}=+\s*$", re.MULTILINE)

    # test for a h1 headings
    if not H1_RE.search(markdown) and not H1_RE_2.search(markdown):
        # Add missing h1 heading to the top of the page
        return page_heading + markdown
    return markdown