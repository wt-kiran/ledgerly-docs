# Deployment after preview approval only

## Current state recorded read-only on 1 November 2026

The existing public repository is wt-kiran/ledgerly-docs. GitHub Pages is **legacy branch publishing, main / (root)**, with custom domain **ledgerly-app.com** and HTTPS enforced. The certificate is approved. No DNS, repository visibility, release assets, Pages settings, remote branch or deployed site was changed during this work. The checkout is local branch `preview/v3.8.5-complete-guide`.

## Review before any public write

Review the local site, field/PDF coverage and discrepancy reports supplied separately. They flag actual access-control, importer, tax and recovery limitations. Obtain the owner's explicit approval of the preview and of the deployment transition below. Do not open a PR or push this branch merely to obtain a preview: all work is already locally reviewable.

## Approved transition to Material/MkDocs

MkDocs generates a static site; the current default Jekyll branch build must not accidentally process its source as the live website. After approval:

1. Keep the existing main commit and Pages configuration record for rollback. Keep the existing release assets untouched.
2. Push the reviewed branch and use a reviewed PR; `Check documentation (no deployment)` builds an artifact only and has no Pages write permission.
3. Coordinate the approved merge with the Pages source change: in repository Settings → Pages, change Build and deployment Source from branch/legacy to **GitHub Actions**. Do not change the custom domain, DNS, visibility or HTTPS setting. This workflow-mode change is required for the supplied standard Actions deployment and has **not** been made automatically.
4. Merge the approved source to main. No push/merge trigger deploys this site automatically.
5. In Actions, manually run **Publish approved documentation** on main with approval input `PUBLISH LEDGERLY DOCS`. Protect the github-pages environment with an owner reviewer if available. The workflow refuses to deploy from any other branch or with a different approval string and refuses legacy mode instead of changing settings.
6. Verify the deployed domain, HTTPS, home/guide/search, mobile/dark theme and both installer links. The workflow publishes only generated `site/` through GitHub Pages; it does not upload/change releases.

Both root CNAME and docs/CNAME retain ledgerly-app.com. Production canonical links use https://ledgerly-app.com/. There is no Sites/Cloudflare hosting registration or DNS operation.

## Rollback

If the approved deployment needs reversal, use the recorded prior main revision and legacy Pages source settings under owner supervision. Do not delete or replace release assets. Keep current sources in a branch before reverting. Check DNS/custom-domain/HTTPS values rather than changing them to troubleshoot content.

## Framework maintenance

This site deliberately uses requested MkDocs 1.6.1 and Material 9.8.0. Material's build emits an upstream support-lifecycle notice (end of life 5 May 2027). Record this for future maintenance; no different framework was substituted. Official workflow reference: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages . Font privacy configuration follows https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/ .
