#!/bin/bash

# PostgreSQL 16 to 18 Migration - Backup Script
# Run this BEFORE upgrading to PostgreSQL 18

set -e

echo "=== PostgreSQL 16 Backup Before Upgrade ==="

# Configuration
CONTAINER_NAME="postgres-cognee"
BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
DB_USER="cognee_user"
DB_NAME="cognee_db"

# Create backup directory
mkdir -p "$BACKUP_DIR"

echo "Creating backup directory: $BACKUP_DIR"

# Check if container is running
if ! docker ps | grep -q $CONTAINER_NAME; then
    echo "❌ PostgreSQL container is not running!"
    echo "Please start your Enhanced Cognee stack first:"
    exit 1
fi

echo "✅ PostgreSQL container found and running"

# 1. Full database backup
echo "📦 Creating full database backup..."
docker exec $CONTAINER_NAME pg_dump \
    -U $DB_USER \
    -d $DB_NAME \
    --format=custom \
    --compress=9 \
    --verbose \
    --file=/tmp/full_backup.dump

docker cp $CONTAINER_NAME:/tmp/full_backup.dump "$BACKUP_DIR/full_backup.dump"

# 2. Check PostgreSQL version
echo "🐘 Checking current PostgreSQL version..."
docker exec $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME -c "SELECT version();" > "$BACKUP_DIR/postgresql_version.txt"

# 3. List all databases
echo "📚 Creating database list..."
docker exec $CONTAINER_NAME psql \
    -U $DB_USER \
    -d postgres \
    -c "\l" > "$BACKUP_DIR/database_list.txt"

echo ""
echo "🎉 Backup completed successfully!"
echo "📁 Backup location: $BACKUP_DIR"
echo "📋 Files created:"
ls -la "$BACKUP_DIR"

echo ""
echo "🚀 Ready for PostgreSQL 18 upgrade!"