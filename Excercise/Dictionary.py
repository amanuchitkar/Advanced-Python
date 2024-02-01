input = input("Enter to search in dictionary: ")
d = {
    "hello": "नमस्ते",
    "aman": "एक आदमी",
    "name": "नाम",
    "computer": "संगणक",
    "coding": "संकेत-वर्गीकरण",
    "education": "शिक्षा",
}
i = input.capitalize()
print(i, " = ", d[input])
