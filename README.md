# Jenna Bortnick: Creative Portfolio

A responsive, static portfolio for GitHub Pages. White, blue, and gold styling follows Jenna’s shared design reference, using supplied portraits, project imagery, and selected presentation pages.

## Preview locally

Requires Python 3.9 or newer; no packages or installation required.

```sh
python3 build.py
python3 tools/check_site.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. You can also open `dist/index.html` directly. The generated site contains ordinary HTML, CSS, JavaScript, and images.

## Current live deployment

- Website: https://jennabortnick.github.io/jenna-portfolio/
- Repository: https://github.com/jennabortnick/jenna-portfolio
- Source code: `main` branch; published files: `gh-pages` branch.

GitHub Pages currently uses **Deploy from a branch → gh-pages → / (root)**. The account’s billing lock blocked custom Actions, so the prebuilt static files use GitHub’s Pages publishing service instead. The optional custom workflow is manual only.

After editing, commit and push your source changes to `main`, then publish with:

```sh
python3 tools/publish.py
```

This builds and checks the site, then updates only the `gh-pages` branch. It requires Git and authenticated push access. The repository now belongs to Jenna. The local `origin` remote points to her repository, and GitHub Pages serves the address above.

## Publish on Jenna’s GitHub account

1. Create a repository in Jenna’s account. Use `JENNAS-USERNAME.github.io` for an account homepage, or any repository name for a project site.
2. Upload this folder’s contents, including the hidden `.github` folder, to the repository’s `main` branch. Using Git or GitHub Desktop is the easiest way to preserve that folder.
3. In the repository’s **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source.
4. Open **Actions → Deploy portfolio to GitHub Pages** and run the workflow if it has not already started. The optional workflow is manually triggered; enable its push trigger if automatic deployment is desired.

The included workflow builds `dist`, validates local links, and deploys it. Relative links support both account and repository sites. See [GitHub’s custom workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

For a custom domain, add a root `CNAME` file containing only the domain name, rebuild, and configure the domain under repository **Settings → Pages**. Follow GitHub’s displayed DNS instructions. The build automatically includes `CNAME` when present.

## Edit the site

- `content/site.json`: project titles, descriptions, credits, gallery selections, and contact links.
- `build.py`: page content and shared layout.
- `styles.css`: colors, typography, and responsive layouts.
- `script.js`: mobile navigation, project filtering, and enlarged image galleries.
- `assets/images`: optimized supplied images.
- `dist`: generated website; regenerate after edits.

Add a public email, LinkedIn URL, or resume path in `content/site.json` when ready. Empty fields stay hidden. For a resume, place its PDF in `assets`, set `resume` to `assets/resume.pdf`, and rebuild. Contact links open email and LinkedIn directly; there is no contact form or backend.

## Content to confirm before public launch

- Jenna’s individual contributions and full team credits for the collaborative projects. Blue Horizon’s floorplan explicitly credits Jenna; the remaining responsibilities are not invented.
- Ibiza Skylink now includes maps, concept visuals, precedents, and atmosphere references from the supplied presentation. The title slide is the cover, with personal names and presentation navigation removed; project credits appear in the page text.
- Raceway USA includes the horse sculpture; digital environment/course layouts belong to Outlaw City, as confirmed by Jenna.
- The supplied résumé is available from About and Contact as an unchanged PDF.
- Academic feasibility figures represent coursework, not actual business results.

The supplied MOV video was reviewed but omitted because its project association is unconfirmed. Original PDFs were not published: selected pages were optimized for the web, and instructor feedback/appendices were excluded. Review the selected presentation pages and any third-party references within them before launch.

## Verification

The link checker checks all generated HTML pages for existing local link/image targets, image alt attributes, titles, viewports, and one primary heading. Browser checks covered desktop/mobile layouts, the mobile menu, project filters, and the enlarged image dialog.

## Asset notes

Ceramics imagery and descriptions were imported from Jenna’s existing portfolio at https://portfolio-xeurons.format.com/ with the user’s instruction. Costume imagery was excluded from the Ceramics page. Seven collections contain twelve images. Names on five presentation slides were removed for display; collaborative credits remain in the project copy/captions. The homepage uses the supplied portrait of Jenna.
