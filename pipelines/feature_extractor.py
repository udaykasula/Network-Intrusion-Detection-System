def extract_features(packet):
    """
    Extract features from packet data.

    Args:
        packet (dict): A dictionary containing packet data.

    Returns:
        list: A list of extracted features.
    """
    try:
        # Extract features with default values if keys are missing
        features = [
            len(packet.get("src", "")),  # Length of source address
            len(packet.get("dst", "")),  # Length of destination address
            int(packet.get("proto", 0)),  # Protocol (ensure it's an integer)
            int(packet.get("len", 0))    # Packet length (ensure it's an integer)
        ]
        # Add placeholders for any additional features used during training
        # Example: Add dummy values for one-hot encoded categories
        features.extend([0] * 14)  # Adjust the number to match the missing features
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid packet data: {packet}. Error: {e}")

    return features
