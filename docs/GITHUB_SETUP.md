# GitHub Repository Setup & VPS Deployment Guide

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `hungry-hippo`
3. Description: `Monaco Electric Construction Services - Emergency Modernism Design`
4. Make it **Public** (required for GitHub Container Registry free tier)
5. Do **NOT** initialize with README (we already have files)
6. Click "Create repository"

## Step 2: Push Code to GitHub

```bash
cd /home/pook/engineer-team/projects/hungry-hippo

# Add GitHub remote (replace YOUR_USERNAME with pookNast)
git remote add origin https://github.com/pookNast/hungry-hippo.git

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Emergency Modernism design for Monaco Electric

- FastAPI backend with HTMX endpoints
- Tailwind CSS oklch color system
- 130-point UX/UI compliance
- Emergency CTA with crosshair cursor
- Feedback widget (22s delay)
- Dynamic favicon (dark/light mode)
- Schema.org LocalBusiness integration
- Docker multi-stage build
- GitHub Actions CI/CD workflow
- Lighthouse CI configuration (≥98 target)

🦛 Generated with Claude Code
"

# Push to GitHub
git push -u origin main
```

## Step 3: Verify GitHub Actions Build

1. Go to https://github.com/pookNast/hungry-hippo/actions
2. The "Build and Push Docker Image" workflow should start automatically
3. Wait for it to complete (usually 3-5 minutes)
4. Once successful, the container will be available at:
   `ghcr.io/pooknast/hungry-hippo:latest`

## Step 4: Deploy to VPS

### Prerequisites
- VPS with Docker installed
- SSH access to VPS
- Domain name (monacoelectric.com) pointed to VPS IP

### Deployment Steps

```bash
# SSH into VPS
ssh user@your-vps-ip

# Create project directory
mkdir -p /opt/hungry-hippo
cd /opt/hungry-hippo

# Download docker-compose.yml
curl -O https://raw.githubusercontent.com/pookNast/hungry-hippo/main/docker-compose.yml

# Create environment file
cat > .env << 'EOF'
GITHUB_USERNAME=pookNast
DEBUG=False
BUSINESS_PHONE=(239) 237-2899
BUSINESS_EMAIL=info@monacoelectric.com
BUSINESS_LICENSE=EC13009733
EOF

# Pull and start the container
docker-compose pull
docker-compose up -d

# Verify it's running
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Monaco Electric Construction Services",
  "performance_targets": {
    "lighthouse": "≥98",
    "js_size": "<12KB",
    "cls": "0.0",
    "lcp": "<2.5s"
  }
}
```

## Step 5: Configure Nginx Reverse Proxy

```bash
# Install Nginx
sudo apt update
sudo apt install nginx -y

# Create Nginx configuration
sudo nano /etc/nginx/sites-available/hungry-hippo
```

Paste this configuration:
```nginx
server {
    listen 80;
    server_name monacoelectric.com www.monacoelectric.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/hungry-hippo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Step 6: Set Up SSL with Let's Encrypt

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain certificate
sudo certbot --nginx -d monacoelectric.com -d www.monacoelectric.com

# Verify auto-renewal
sudo certbot renew --dry-run
```

## Continuous Deployment

Every push to the `main` branch will:
1. Trigger GitHub Actions workflow
2. Build new Docker image
3. Push to `ghcr.io/pooknast/hungry-hippo:latest`

To update your VPS after pushing changes:

```bash
ssh user@your-vps-ip
cd /opt/hungry-hippo
docker-compose pull
docker-compose up -d
```

## Monitoring & Troubleshooting

### View Logs
```bash
docker-compose logs -f app
```

### Check Container Health
```bash
docker ps
docker inspect hungry-hippo
```

### Performance Verification
```bash
# Install Lighthouse CI locally
npm install -g @lhci/cli

# Run audit (replace with your domain)
lhci collect --url=https://monacoelectric.com
```

Expected scores:
- Performance: ≥98
- Accessibility: 100
- Best Practices: ≥95
- SEO: 100

## Project Structure on VPS

```
/opt/hungry-hippo/
├── docker-compose.yml
├── .env
└── (Docker volumes managed by Docker Compose)
```

## Backup Strategy

```bash
# Backup environment configuration
cp /opt/hungry-hippo/.env ~/backups/hungry-hippo-env-$(date +%Y%m%d).bak

# When database is implemented:
docker exec hungry-hippo-db pg_dump -U postgres > backup_$(date +%Y%m%d).sql
```

## Troubleshooting

**Container won't start:**
```bash
docker-compose logs app
docker inspect hungry-hippo
```

**Port 8000 already in use:**
```bash
sudo lsof -i :8000
sudo kill -9 <PID>
```

**Permission issues:**
```bash
sudo chown -R 1000:1000 /opt/hungry-hippo
```

## Support

For issues with the deployment:
- Check GitHub Actions: https://github.com/pookNast/hungry-hippo/actions
- Review container logs: `docker-compose logs -f`
- Verify health endpoint: `curl http://localhost:8000/health`
