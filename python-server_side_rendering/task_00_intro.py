def generate_invitations(template, attendees):
    if not isinstance(template, str) or not (isinstance(attendees, list) and all(isinstance(a, dict) for a in attendees)):
        print("template must be a string and attendees a list of dictionaries")
        return

    if not template.strip():
        print(("Template is empty, no output files generated."))
        return

    if len(attendees) == 0:
        print(("No data provided, no output files generated."))
        return

    for i in range(len(attendees)):
        invitation = template.replace("{name}", attendees[i].get("name") or "N/A") \
                                .replace("{event_title}", attendees[i].get("event_title") or "N/A") \
                                .replace("{event_date}", attendees[i].get("event_date") or "N/A") \
                                .replace("{event_location}", attendees[i].get("event_location") or "N/A")
        try:
            with open(f"output_{i + 1}.txt", 'w') as f:
                f.write(invitation)
        except OSError as e:
            print(f"Couldn't write the invitation file {i}. Error: {e}")
