#!/bin/sh
tee /etc/redis/sentinel.conf <<EOF
port 26379
daemonize yes
logfile "/var/log/sentinel.log"
pidfile "var/run/sentinel.pid"
dir "/var/lib/redis/sentinel"

sentinel monitor docker-cluster redis-slave 6379 2
sentinel down-after-milliseconds docker-cluster 5000
sentinel parallel-syncs docker-cluster 1
sentinel failover-timeout docker-cluster 1000

EOF

redis-sentinel /etc/redis/sentinel.conf