"""Track supplier purchase orders and warehouse deliveries."""

import sqlite3


def create_connection():
    """Create an in-memory database for purchase orders."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            supplier TEXT,
            item TEXT,
            quantity INTEGER,
            received INTEGER,
            remarks TEXT
        )
        """
    )
    return connection


def place_order(connection, supplier, item, quantity):
    """Insert a new purchase order and return the total quantity."""
    connection.execute(
        """
        INSERT INTO orders (supplier, item, quantity, received, remarks)
        VALUES (?, ?, ?, 0, NULL)
        """,
        (supplier, item, quantity),
    )
    return total_order_quantity(connection)


def mark_received(connection, order_id, remarks):
    """Mark an order as received and record delivery remarks."""
    connection.execute(
        """
        UPDATE orders
        SET received = 1, remarks = ?
        WHERE id = ?
        """,
        (remarks, order_id),
    )


def notify_warehouse(supplier):
    """Display a warehouse notification without running a shell."""
    print(f"Notifying warehouse about {supplier}")


def cleanup(connection):
    """Delete orders that have already been received."""
    connection.execute("DELETE FROM orders WHERE received = 1")


def pending_count(connection):
    """Return the number of orders that are still pending."""
    result = connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    )
    return result.fetchone()[0]


def total_order_quantity(connection):
    """Return the sum of all order quantities."""
    result = connection.execute("SELECT SUM(quantity) FROM orders")
    return result.fetchone()[0] or 0


def main():
    """Run a demonstration of the purchase order tracker."""
    connection = create_connection()
    try:
        place_order(connection, "Acme Steel", "rods", 40)
        place_order(connection, "Bolt Co", "bolts", 500)
        mark_received(connection, 1, "ok")
        notify_warehouse("Acme")
        connection.commit()
        print(pending_count(connection), total_order_quantity(connection))
        cleanup(connection)
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
