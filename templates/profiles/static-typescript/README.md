# Static TypeScript Profile

For static web apps, dashboards, and client-side tools.

Apply [security watchouts](../../../agents/rules/security-watchouts.md) when adding public assets, APIs or deployment. TypeScript types disappear at runtime; browser inputs, API responses and stored records still need validation. Everything delivered to a browser is public, including source maps and embedded configuration.

Consider adding:

- `workspace/src/`
- `workspace/public/`
- `workspace/package.json`
- `workspace/tsconfig.json`
- `workspace/vite.config.ts`

Common ignored outputs:

- `workspace/node_modules/`
- `workspace/dist/`
- `.vite/`
