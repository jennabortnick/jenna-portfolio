# Jenna Bortnick — Creative Portfolio

A responsive, static portfolio for GitHub Pages. White, blue, and gold styling follows Jenna’s shared design reference, using supplied portraits, project imagery, and selected presentation pages.

## Preview locally

Requires Python 3.9 or newer; no packages or installation required.

```sh
python3 build.py
python3 tools/check_site.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. You can also open `dist/index.html` directly. The generated site contains ordinary HTML, CSS, JavaScript, and images.

## Publish on Jenna’s GitHub account

1. Create a repository in Jenna’s account. Use `JENNAS-USERNAME.github.io` for an account homepage, or any repository name for a project site.
2. Upload this folder’s contents, including the hidden `.github` folder, to the repository’s `main` branch. Using Git or GitHub Desktop is the easiest way to preserve that folder.
3. In the repository’s **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source.
4. Open **Actions → Deploy portfolio to GitHub Pages** and run the workflow if it has not already started. Each later push to `main` rebuilds and deploys the site.

The included workflow builds `dist`, validates local links, and deploys it. Relative links support both account and repository sites. See [GitHub’s custom workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

For a custom domain, add a root `CNAME` file containing only the domain name, rebuild, and configure the domain under repository **Settings → Pages**. Follow GitHub’s displayed DNS instructions. The build automatically includes `CNAME` when present.

## Edit the site

- `content/site.json`: project titles, descriptions, credits, gallery selections, and contact links.
- `build.py`: page content and shared layout.
- `styles.css`: colors, typography, and responsive layouts.
- `script.js`: mobile navigation, project filtering, and enlarged image galleries.
- `assets/images`: optimized supplied images.
- `dist`: generated website; regenerate after edits.

Add a public email, LinkedIn URL, or resume path in `content/site.json` when ready. Empty fields stay hidden. For a resume, place its PDF in `assets`, set `resume` to `assets/resume.pdf`, and rebuild. Contact is currently informational; there is no contact form or backend.

## Content to confirm before public launch

- Jenna’s individual contributions and full team credits for the collaborative projects. Blue Horizon’s floorplan explicitly credits Jenna; the remaining responsibilities are not invented.
- Original Ibiza Skylink presentation and imagery. Its current title graphic was created for this site and is not presented as project artwork.
- Which supplied modelmaking and Blender studies belong to Raceway USA and Outlaw City. Current selections are provisional and identified as process studies.
- Public contact information and resume.
- Academic feasibility figures represent coursework, not actual business results.

The supplied MOV video was reviewed but omitted because its project association is unconfirmed. Original PDFs were not published: selected pages were optimized for the web, and instructor feedback/appendices were excluded. Review the selected presentation pages and any third-party references within them before launch.

## Verification

The link checker checks all generated HTML pages for existing local link/image targets, image alt attributes, titles, viewports, and one primary heading. Browser checks covered desktop/mobile layouts, the mobile menu, project filters, and the enlarged image dialog.
