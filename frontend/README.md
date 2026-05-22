This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Administrative Interface & Multi-User Architecture

The `frontend/` directory now includes an exclusive administrative dashboard (`/admin`) protected by Firebase Authentication. This architecture enables secure, multi-user access to the Sovereign Context Engineering Workspace.

### Architecture Highlights
1.  **Firebase Integration**: Core initialization is handled in `src/lib/firebase.ts`. Environment variables (e.g., `NEXT_PUBLIC_FIREBASE_API_KEY`) define the active Firebase instance.
2.  **Contextual Authentication**: `src/context/AuthContext.tsx` wraps the entire application, providing real-time `user` state and `loading` status to all components.
3.  **Protected Routes**: The `/admin` path and its sub-components use client-side hooks to verify the authentication state. Unauthenticated requests are aggressively routed to the `/login` view.
4.  **Bicameral Navigation**: The root path (`/`) acts merely as a router, redirecting users to `/admin`, enforcing the administrative-first paradigm of the UI.
