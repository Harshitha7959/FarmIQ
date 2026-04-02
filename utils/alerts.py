def generate_alerts(humidity):
    if humidity > 70:
        return "⚠ High humidity - Risk of fungal disease"
    else:
        return "✅ Weather conditions are safe"
