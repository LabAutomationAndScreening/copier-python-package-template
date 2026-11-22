---
paths:
  - "**/*.{ts,ts.jinja,vue,vue.jinja,mts,mjs,mjs.jinja}"
  # In a template repository, a file rendered only on a condition has a name that ends in a Jinja tag, such as x.ts{% endif %} or x.ts{% endif %}.jinja. "?%" matches the "{%" that follows the extension.
  - "**/*.{ts,vue,mts,mjs}?%*"
---
# TypeScript

- For frontend tests, run commands via `pnpm` scripts from the frontend package's `package.json` (`frontend/package.json` where the frontend has its own directory) — never invoke tools directly (not pnpm exec <tool>, npx <tool>, etc.). ✅ pnpm test-unit  ❌ pnpm vitest ... or npx vitest ...
- Key `pre-commit` hook IDs for TypeScript: `typescript-check`, `eslint`.

<!--
============== WARNING ==============================================================================
File is managed by copier template: gh:LabAutomationAndScreening/copier-base-template.git
See .config/.copier-managed-files.json for details.

You are welcome to make changes to this file in your repo if they are custom to your project,
but if the change should be shared with other projects, please backport it to the template repo.
=====================================================================================================
-->
