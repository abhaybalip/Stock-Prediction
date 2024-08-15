import { headers } from 'next/headers';
import { NextResponse, NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
    var response = NextResponse.json({ "message": "Hi,its working" }, {
        status: 200, headers: {}
    })
    response.headers.set('key','value')

    return response
}

export async function HEAD(request: NextRequest) {
    // HEAD requests usually respond with headers similar to GET but without a body
    return new NextResponse(null, { status: 200 });
}

export async function POST(request: NextRequest) {
    // Handle POST request, typically involving reading request body
    const data = await request.json();
    return NextResponse.json({
        message: "POST request received",
        data: data
    });
}

export async function PUT(request: NextRequest) {
    // Handle PUT request, typically involving updating resources
    const data = await request.json();
    return NextResponse.json({
        message: "PUT request received",
        data: data
    });
}

export async function DELETE(request: NextRequest) {
    // Handle DELETE request, typically involving deleting resources
    return NextResponse.json({
        message: "DELETE request received"
    });
}

export async function PATCH(request: NextRequest) {
    // Handle PATCH request, typically involving partial updates
    const data = await request.json();
    return NextResponse.json({
        message: "PATCH request received",
        data: data
    });
}

export async function OPTIONS(request: NextRequest) {
    // OPTIONS request, generally used to describe the communication options for the target resource
    return new NextResponse(null, {
        status: 204,
        headers: {
            'Allow': 'GET, HEAD, POST, PUT, DELETE, PATCH, OPTIONS'
        }
    });
}
