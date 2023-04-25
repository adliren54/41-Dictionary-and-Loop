print("🌟Website Rating🌟")

web = input("\nInput the website name: ")
url = input("\nInput the URL: ")
desc = input("\nInput your a description: ")
star = input("\nInput the rating out of 5: \n")

dictinary = {"name": web, "url": url, "description": desc, "star": star}

for name, value in dictinary.items():
  print(f"{name}:{value}")