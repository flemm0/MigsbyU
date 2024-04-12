#!/bin/bash

# check if Debezium connector is available

check_debezium() {
    curl -s -o /dev/null http://debezium:8083/connectors
}

echo "Waiting for Debezium setup..."
until check_debezium; do
    echo "Debezium is not ready yet. Retrying in 5 seconds..."
    sleep 5
done

echo "Debezium setup completed. Proceeding with the command."

sh -c "curl -i -X POST -H 'Content-Type: application/json' --data @/debezium/debezium.json http://debezium:8083/connectors"