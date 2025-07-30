import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
    const skip_url_paths = ["/login", "/register", "/logout", "/_next", "/favicon.ico"]
    const pathname = request.nextUrl.pathname;
    const token = request.cookies.get("token") || true;

    const path_matched = skip_url_paths.some((path) => pathname.startsWith(path))
    if (path_matched) {
        return NextResponse.next()

    }

    if (!token) {
        return NextResponse.redirect(new URL("/login", request.url));
    }

}

