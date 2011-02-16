#!/bin/bash
mysqldump --opt colors | gzip -c | ssh rich@zenla 'cat > ~/Backups/mysql-$(date +%Y%m%d).gz'
