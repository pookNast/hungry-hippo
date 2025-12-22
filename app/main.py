"""
Hungry-Hippo FastAPI Application
Emergency Modernism Design for Monaco Electric Construction Services

Tech Stack:
- FastAPI (async Python web framework)
- HTMX (server-side hypermedia)
- Alpine.js (surgical client-side reactivity <12KB)
- Jinja2 (template engine)
- Tailwind CSS (oklch color system)

Performance Targets:
- Lighthouse ≥ 98
- Total JS < 12KB gzipped
- CLS = 0.0
- LCP < 2.5s
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Monaco Electric Construction Services",
    description="24/7 Emergency Electrical Service in Fort Myers & Cape Coral",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Pydantic models for data validation
class FeedbackModel(BaseModel):
    reaction: str  # ⚡ (love), 😕 (confused), 😟 (sad)
    comment: Optional[str] = None

class QuoteRequestModel(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service_type: str
    message: Optional[str] = None

class DispatchStatusModel(BaseModel):
    technicians_available: int
    avg_response_time_hours: float
    current_calls: int


# Routes
@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """
    Homepage with Emergency Modernism design
    Asymmetric layout, emergency-first CTA, oklch colors
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "business_name": "Monaco Electric Construction Services",
            "phone": "(239) 237-2899",
            "license": "EC13009733",
            "service_areas": ["Fort Myers", "Cape Coral", "Bonita Springs", "Estero"],
        }
    )


@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    """Services page with circuit breaker panel metaphor"""
    return templates.TemplateResponse(
        "services.html",
        {"request": request}
    )


@app.get("/service-area", response_class=HTMLResponse)
async def service_area(request: Request):
    """Service area page with map"""
    return templates.TemplateResponse(
        "service-area.html",
        {"request": request}
    )


@app.get("/quote", response_class=HTMLResponse)
async def quote_form(request: Request):
    """Quote request form with Alpine.js validation"""
    return templates.TemplateResponse(
        "quote.html",
        {"request": request}
    )


# HTMX Endpoints (Progressive Enhancement)
@app.get("/partials/service-area-map", response_class=HTMLResponse)
async def service_area_map_partial(request: Request):
    """
    HTMX partial for service area map
    Lazy-loaded via hx-trigger="intersect once"
    """
    return templates.TemplateResponse(
        "partials/service-area-map.html",
        {
            "request": request,
            "service_areas": [
                {"name": "Fort Myers", "icon": "map-pin"},
                {"name": "Cape Coral", "icon": "map-pin"},
                {"name": "Bonita Springs", "icon": "map-pin"},
                {"name": "Estero", "icon": "map-pin"},
            ]
        }
    )


@app.post("/api/feedback")
async def submit_feedback(feedback: FeedbackModel):
    """
    Feedback widget POST handler
    Receives reaction (⚡😕😟) and optional comment
    """
    # TODO: Store feedback in database
    # TODO: Send notification to business owner

    return {
        "success": True,
        "message": "Thank you for your feedback!",
        "reaction": feedback.reaction,
    }


@app.get("/api/dispatch-status", response_class=HTMLResponse)
async def dispatch_status(request: Request):
    """
    Live dispatch status for hx-swap-oob
    Updates every 30s via hx-trigger="every 30s"
    """
    # TODO: Get real-time data from dispatch system
    status = DispatchStatusModel(
        technicians_available=2,
        avg_response_time_hours=2.0,
        current_calls=3
    )

    return templates.TemplateResponse(
        "partials/dispatch-status.html",
        {
            "request": request,
            "status": status
        }
    )


@app.post("/quote", response_class=HTMLResponse)
async def submit_quote(
    request: Request,
    name: str = Form(...),
    email: EmailStr = Form(...),
    phone: str = Form(...),
    service_type: str = Form(...),
    message: Optional[str] = Form(None)
):
    """
    Quote form submission with progressive enhancement
    Works with JS disabled (standard POST)
    Enhanced with HTMX for no-refresh submission
    """
    quote_request = QuoteRequestModel(
        name=name,
        email=email,
        phone=phone,
        service_type=service_type,
        message=message
    )

    # TODO: Store quote request in database
    # TODO: Send email notification
    # TODO: Add to CRM system

    # Return success template (HTMX will swap this in)
    return templates.TemplateResponse(
        "partials/quote-success.html",
        {
            "request": request,
            "name": name
        }
    )


# 404 Handler (Circuit Breaker Theme)
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse(
        "404.html",
        {"request": request},
        status_code=404
    )


# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Monaco Electric Construction Services",
        "performance_targets": {
            "lighthouse": "≥98",
            "js_size": "<12KB",
            "cls": "0.0",
            "lcp": "<2.5s"
        }
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
