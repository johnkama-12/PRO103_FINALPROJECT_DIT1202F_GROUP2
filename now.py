import customtkinter as ctk
from tkinter import messagebox, filedialog
from datetime import datetime
import calendar as cal
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import copy
import json
import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ============ CONFIGURATION ============
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ============ STUDENTS FILE ============
STUDENTS_FILE = "students.json"

def load_students():
    global STUDENTS
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            STUDENTS = json.load(f)

def save_students():
    with open(STUDENTS_FILE, "w") as f:
        json.dump(STUDENTS, f, indent=2)

def generate_student_id():
    while True:
        new_id = f"ST-{random.randint(100000, 999999)}"
        if not any(s["id"] == new_id for s in STUDENTS):
            return new_id

def send_welcome_email(email, student_id, name, password):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "pythonlogger4@gmail.com"
    SENDER_PASSWORD = "ghae tkqv dbgp uoqs"
    
    try:
        msg = MIMEMultipart()
        msg["From"] = f"Limkokwing Student Portal <{SENDER_EMAIL}>"
        msg["To"] = email
        msg["Subject"] = "🎓 Welcome to Limkokwing Student Portal - Your Account Details"
        
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; padding: 20px; background: #f8fafc;">
            <div style="max-width: 500px; margin: 0 auto;">
                <div style="background: #1a3a6b; padding: 25px; border-radius: 12px 12px 0 0; text-align: center;">
                    <h1 style="color: #fbbf24; margin: 0;">🎓 Limkokwing Student Portal</h1>
                    <p style="color: #bfdbfe; margin: 5px 0 0 0;">Learning Management System</p>
                </div>
                <div style="background: white; padding: 25px; border-radius: 0 0 12px 12px; border: 1px solid #e2e8f0;">
                    <h2 style="color: #1a3a6b;">Hello {name},</h2>
                    <p style="color: #64748b;">Your student account has been created successfully!</p>
                    <div style="background: #f1f5f9; padding: 20px; border-radius: 10px; margin: 20px 0;">
                        <h3 style="color: #1a3a6b; margin-top: 0;">Your Login Credentials:</h3>
                        <div style="background: white; padding: 12px; border-radius: 8px; margin: 10px 0;">
                            <strong>Student ID:</strong> 
                            <span style="background: #dbeafe; padding: 6px 12px; border-radius: 6px; font-size: 16px;">{student_id}</span>
                        </div>
                        <div style="background: white; padding: 12px; border-radius: 8px;">
                            <strong>Password:</strong> 
                            <span style="background: #fef9c3; padding: 6px 12px; border-radius: 6px;">{password}</span>
                        </div>
                    </div>
                    <p style="color: #64748b;">You can log in at the Limkokwing Student Portal.</p>
                    <div style="background: #fef2f2; padding: 12px; border-radius: 8px; margin-top: 15px;">
                        <p style="color: #dc2626; font-size: 12px; margin: 0;">
                            ⚠️ Please keep your credentials safe. Change your password in Settings after logging in.
                        </p>
                    </div>
                </div>
                <p style="text-align: center; color: #94a3b8; font-size: 11px; margin-top: 15px;">
                    © 2024 Limkokwing Student Portal. All rights reserved.
                </p>
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(body, "html"))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        
        if not SENDER_PASSWORD:
            print("Email sending skipped: set EMAIL_APP_PASSWORD environment variable to enable SMTP.")
            return False
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

# ============ DATA ============
STUDENTS = [
    {"id": "905006475", "name": "Chris Effionga", "password": "chris123", 
     "avatar": "CE", "grade": "15 points Year 1"},
    {"id": "905007895", "name": "Mohamed Tucker", "password": "Moh123", 
     "avatar": "MT", "grade": "14 point Year 2"},
    {"id": "905006789", "name": "Caro", "password": "Caro123", 
     "avatar": "CA", "grade": "14 point Year 3"}
]

COURSES = [
    {"name": "Computerise Mathematics", "code": "MATH-401", 
     "teacher": "Mr. Amadu Kamara", "progress": 78, "grade": "B+", 
     "score": 88, "students": 28, "color": "#1a3a6b", "next": "Properties of integer"},
    {"name": "Software Engineering", "code": "SOF-301", 
     "teacher": "Mr. Hassan Kamara", "progress": 64, "grade": "A-", 
     "score": 91, "students": 24, "color": "#f59e0b", "next": "Designing with Figma"},
    {"name": "Multimedia", "code": "MUL-201", "teacher": "Mr. Tappiah",
     "progress": 91, "grade": "A", "score": 95, "students": 22, 
     "color": "#10b981", "next": "Bouncing ball"},
    {"name": "Structured Programming", "code": "PROG-301", 
     "teacher": "Mr. Elijah", "progress": 55, "grade": "B", 
     "score": 83, "students": 30, "color": "#8b5cf6", "next": "Control Structures"},
    {"name": "Database Management", "code": "DAT-301", 
     "teacher": "Mr. Jelil", "progress": 70, "grade": "B+", 
     "score": 87, "students": 20, "color": "#ef4444", "next": "MySQL with XAMPP"},
    {"name": "Data Communication", "code": "DC-201", 
     "teacher": "Mr. Sahid", "progress": 82, "grade": "A", 
     "score": 96, "students": 18, "color": "#0891b2", "next": "Sorting Algorithms"}
]

UPCOMING = [
    {"subj": "Computerise Mathematics", "task": "Chapter 7 Problem Set", 
     "due": "Today, 11:59 PM", "urg": True},
    {"subj": "Multimedia", "task": "Moving Character", 
     "due": "Tomorrow, 9:00 AM", "urg": True},
    {"subj": "Datacommunication", "task": "Lab1 Cisco Packet Tracer", 
     "due": "Jun 14, 5:00 PM", "urg": False},
    {"subj": "Software Engineering", "task": "Figma Design", 
     "due": "Jun 16, 11:59 PM", "urg": False}
]

ASSIGNMENTS = [
    {"id": 1, "subj": "DataCommunication", "title": "Cisco Packet Configuration",
     "due": "Jun 12, 2025", "status": "pending", "urg": True, "pts": 50},
    {"id": 2, "subj": "Structure Programming", "title": "Object Oriented Programming",
     "due": "Jun 13, 2025", "status": "pending", "urg": True, "pts": 100},
    {"id": 3, "subj": "Software Engineering", "title": "Fundamentals in developing software",
     "due": "Jun 14, 2025", "status": "pending", "urg": False, "pts": 75},
    {"id": 4, "subj": "Database", "title": "Data Definition Language",
     "due": "Jun 10, 2025", "status": "graded", "urg": False, "pts": 40, 
     "grade": "A", "score": "38/40"},
    {"id": 5, "subj": "Computerise Mathematics", "title": "Properties of an integer",
     "due": "Jun 5, 2025", "status": "graded", "urg": False, "pts": 100, 
     "grade": "B+", "score": "88/100"},
    {"id": 6, "subj": "Multimedia", "title": "Animation",
     "due": "Jun 8, 2025", "status": "submitted", "urg": False, "pts": 80}
]

CONVOS = [
    {"id": 1, "name": "Mr. Amadu Kamara", "role": "Computerise Mathematics", 
     "av": "AK", "unread": 1, "last": "Great work on the midterm!",
     "msgs": [
         {"f": "them", "t": "Hi Chris! Your midterm scored 88/100!", "tm": "Jun 10, 10:00 AM"},
         {"f": "me", "t": "Thank you so much!", "tm": "Jun 10, 10:15 AM"},
         {"f": "them", "t": "Let me know if you need help with chapter 7.", "tm": "Today, 10:24 AM"}
     ]},
    {"id": 2, "name": "Mr. Elijah Fullah", "role": "Programming Lecturer", 
     "av": "DT", "unread": 1, "last": "Assignment due tomorrow.",
     "msgs": [{"f": "them", "t": "Don't forget your Programming Assignment is due tomorrow.", "tm": "Yesterday"}]},
    {"id": 3, "name": "Dr. Sahid", "role": "Data Communication", "av": "DS", 
     "unread": 0, "last": "Your lab report looks excellent!",
     "msgs": [
         {"f": "me", "t": "Could you review my lab report?", "tm": "Jun 9"},
         {"f": "them", "t": "Your lab report structure looks excellent!", "tm": "Jun 10"}
     ]}
]

EVENTS = {
    (2025, 6, 12): ["Computerise Mathematics", "Multimedia Lab"],
    (2025, 6, 13): ["Structured Programming", "Data Communication"],
    (2025, 6, 14): ["Database Management", "Software Engineering"],
    (2025, 6, 17): ["Computerise Math Exam"],
    (2025, 6, 19): ["Multimedia Project Due"],
    (2025, 6, 21): ["Data Communication Assignment"],
    (2025, 6, 24): ["Software Engineering Review"],
    (2025, 6, 28): ["Semester Finals Begin"],
}

SCORE_TREND = [78, 82, 79, 85, 88, 84, 91, 87]

C = {
    "primary": "#1a3a6b", "primary_light": "#2a4a7f", "primary_dark": "#0f1929",
    "gold": "#fbbf24", "bg": "#f8fafc", "white": "#ffffff",
    "text": "#0f172a", "text_light": "#64748b", "text_muted": "#94a3b8",
    "border": "#e2e8f0", "blue": "#1d4ed8", "red": "#dc2626",
    "green": "#047857", "amber": "#b45309", "emerald": "#10b981",
    "purple": "#8b5cf6", "cyan": "#0891b2", "sidebar": "#1a3a6b",
    "stat_bg": "#1a2744"
}

# ============ GLOBAL STATE ============
root = None
current_user = None
current_page = "dashboard"
login_view = "login"
cal_yr = 2025
cal_mo = 6
submitted_assignments = set()
nav_buttons = {}
page_container = None
page_title = None
login_id = None
login_pass = None
login_error = None
show_pw = None
signup_vars = {}
signup_subjects_text = None
terms_agreed = None
file_var = None
note_text = None
filter_var = "all"
filter_buttons = {}
assignments_container = None
active_conv = None
conversations = []
chat_container = None
msg_var = None
settings_vars = {}
notif_vars = {}
save_lbl = None
particles = []
particle_canvas = None
particle_running = False

# ============ PARTICLE EFFECTS ============
def start_particles(parent_frame):
    global particle_canvas, particle_running, particles
    particle_canvas = ctk.CTkCanvas(parent_frame, highlightthickness=0)
    particle_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    particles = []
    colors = ["#fbbf24", "#60a5fa", "#34d399", "#f472b6", "#a78bfa", "#fb923c"]
    for _ in range(20):
        particles.append({
            "x": random.randint(0, 1200), "y": random.randint(0, 750),
            "size": random.randint(2, 5), "color": random.choice(colors),
            "speed": random.uniform(0.2, 1.0),
            "dx": random.uniform(-0.3, 0.3), "dy": random.uniform(-0.8, -0.2)
        })
    particle_running = True
    animate_particles()

def animate_particles():
    global particle_canvas, particles, particle_running
    if not particle_running or not particle_canvas:
        return
    try:
        particle_canvas.delete("all")
        w, h = particle_canvas.winfo_width(), particle_canvas.winfo_height()
        for p in particles:
            p["x"] += p["dx"] * p["speed"]
            p["y"] += p["dy"] * p["speed"]
            if p["x"] < -10: p["x"] = w + 10
            if p["x"] > w + 10: p["x"] = -10
            if p["y"] < -10: p["y"] = h + 10
            if p["y"] > h + 10: p["y"] = -10
            x, y, s, c = p["x"], p["y"], p["size"], p["color"]
            particle_canvas.create_oval(x-s*2, y-s*2, x+s*2, y+s*2, fill=c, outline="", stipple="gray25")
            particle_canvas.create_oval(x-s, y-s, x+s, y+s, fill=c, outline="")
        root.after(30, animate_particles)
    except:
        particle_running = False

def stop_particles():
    global particle_running, particle_canvas
    particle_running = False
    if particle_canvas:
        particle_canvas.destroy()
        particle_canvas = None

# ============ HELPERS ============
def grade_color(grade):
    if grade and grade.startswith("A"): return "#dcfce7", "#166534"
    if grade and grade.startswith("B"): return "#fef9c3", "#854d0e"
    return "#fee2e2", "#991b1b"

def clear_window():
    stop_particles()
    for widget in root.winfo_children():
        widget.destroy()


def parse_subjects(subject_text):
    """Convert comma/new-line subject text into a clean list of unique subjects."""
    raw = subject_text.replace("\n", ",").split(",")
    subjects = []
    for item in raw:
        subject = item.strip()
        if subject and subject.lower() not in [s.lower() for s in subjects]:
            subjects.append(subject)
    return subjects

SUBJECT_COLORS = ["#1a3a6b", "#f59e0b", "#10b981", "#8b5cf6", "#ef4444", "#0891b2", "#db2777", "#16a34a"]

def build_courses_from_subjects(subjects):
    """Build course cards from the subjects entered during signup."""
    courses = []
    for i, subject in enumerate(subjects):
        score = 80 + (i * 3) % 16
        progress = 45 + (i * 9) % 50
        grade = "A" if score >= 90 else "B+" if score >= 85 else "B"
        courses.append({
            "name": subject,
            "code": f"SUB-{101 + i}",
            "teacher": "Assigned Lecturer",
            "progress": progress,
            "grade": grade,
            "score": score,
            "students": 1,
            "color": SUBJECT_COLORS[i % len(SUBJECT_COLORS)],
            "next": f"Introduction to {subject}"
        })
    return courses

def get_user_courses():
    """Demo accounts keep the original courses; new signup accounts use their own subjects."""
    if current_user and current_user.get("subjects"):
        return build_courses_from_subjects(current_user["subjects"])
    return COURSES

def get_user_assignments():
    if current_user and current_user.get("subjects"):
        assignments = []
        for i, course in enumerate(get_user_courses(), start=1):
            assignments.append({
                "id": 1000 + i,
                "subj": course["name"],
                "title": f"{course['name']} Assignment {i}",
                "due": f"Jun {12 + i}, 2024",
                "status": "pending" if i % 3 != 0 else "submitted",
                "urg": i <= 2,
                "pts": 100
            })
        return assignments
    return ASSIGNMENTS

def get_user_upcoming():
    if current_user and current_user.get("subjects"):
        return [
            {"subj": course["name"], "task": f"{course['name']} Assignment", "due": f"Jun {13 + i}, 5:00 PM", "urg": i < 2}
            for i, course in enumerate(get_user_courses()[:4])
        ]
    return UPCOMING

def get_user_events():
    if current_user and current_user.get("subjects"):
        events = {}
        for i, course in enumerate(get_user_courses()):
            day = 12 + i
            events[(2025, 6, day)] = [f"{course['name']} Class"]
            if i < 3:
                events[(2025, 6, day + 7)] = [f"{course['name']} Assignment Due"]
        return events
    return EVENTS

def get_user_conversations():
    if current_user and current_user.get("subjects"):
        convs = []
        for i, subject in enumerate(current_user["subjects"], start=1):
            initials = ''.join([w[0] for w in subject.split()[:2]]).upper() or "AL"
            convs.append({
                "id": i,
                "name": "Assigned Lecturer",
                "role": subject,
                "av": initials,
                "unread": 1 if i == 1 else 0,
                "last": f"Welcome to {subject}.",
                "msgs": [
                    {"f": "them", "t": f"Welcome to {subject}. Your first assignment will appear in the assignment page.", "tm": "Today"}
                ]
            })
        return convs
    return copy.deepcopy(CONVOS)

def get_user_score_trend():
    if current_user and current_user.get("subjects"):
        scores = [c["score"] for c in get_user_courses()]
        return scores if len(scores) >= 2 else scores + [scores[0] + 2 if scores else 80]
    return SCORE_TREND

# ============ SIGNUP ============
def signup_submit():
    global signup_vars, signup_subjects_text, terms_agreed, STUDENTS
    
    first = signup_vars.get("first_name", ctk.StringVar()).get().strip()
    last = signup_vars.get("last_name", ctk.StringVar()).get().strip()
    email = signup_vars.get("email", ctk.StringVar()).get().strip()
    student_id = signup_vars.get("student_id", ctk.StringVar()).get().strip()
    institution = signup_vars.get("institution", ctk.StringVar()).get().strip()
    subject_text = signup_subjects_text.get("1.0", "end").strip() if signup_subjects_text else ""
    subjects = parse_subjects(subject_text)
    password = signup_vars.get("password", ctk.StringVar()).get()
    confirm = signup_vars.get("confirm_password", ctk.StringVar()).get()
    
    if not first:
        messagebox.showerror("Missing Fields", "Please enter your First Name.")
        return
    if not last:
        messagebox.showerror("Missing Fields", "Please enter your Last Name.")
        return
    if not email:
        messagebox.showerror("Missing Fields", "Please enter your Email Address.")
        return
    if "@" not in email or "." not in email:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return
    if not institution:
        messagebox.showerror("Missing Fields", "Please enter your Institution/School.")
        return
    if not subjects:
        messagebox.showerror("Missing Subjects", "Please enter at least one subject/course. Example: Programming, Database, Multimedia")
        return
    if not password:
        messagebox.showerror("Missing Fields", "Please enter a Password.")
        return
    if len(password) < 6:
        messagebox.showerror("Password Too Short", "Password must be at least 6 characters.")
        return
    if password != confirm:
        messagebox.showerror("Password Mismatch", "Passwords do not match.")
        return
    if not terms_agreed.get():
        messagebox.showerror("Terms Required", "You must agree to the Terms of Service.")
        return
    
    if not student_id:
        student_id = generate_student_id()
    elif any(s["id"] == student_id for s in STUDENTS):
        messagebox.showerror("ID Exists", "This Student ID already exists.")
        return
    
    new_student = {
        "id": student_id,
        "name": f"{first} {last}",
        "password": password,
        "avatar": f"{first[0]}{last[0]}".upper(),
        "grade": "Year 1",
        "subjects": subjects
    }
    
    STUDENTS.append(new_student)
    save_students()
    
    email_sent = send_welcome_email(email, student_id, new_student["name"], password)
    
    if email_sent:
        msg = (f"Welcome, {first}!\n\nAccount created successfully!\n\n"
               f"📧 A welcome email has been sent to: {email}")
    else:
        msg = (f"Welcome, {first}!\n\nAccount created successfully!\n\n"
               f"⚠️ SAVE YOUR CREDENTIALS:\nStudent ID: {student_id}\nPassword: {password}")
    
    messagebox.showinfo("Account Created", msg)
    set_view("login")

def set_view(view):
    global login_view
    login_view = view
    show_login()

def toggle_password():
    login_pass.configure(show="" if show_pw.get() else "*")

def fill_demo(s):
    login_id.delete(0, "end")
    login_id.insert(0, s["id"])
    login_pass.delete(0, "end")
    login_pass.insert(0, s["password"])

def login():
    global current_user
    load_students()
    sid = login_id.get().strip()
    spass = login_pass.get().strip()
    if not sid or not spass:
        login_error.configure(text="Please fill in all fields")
        return
    student = next((s for s in STUDENTS if s["id"] == sid and s["password"] == spass), None)
    if student:
        current_user = student
        login_error.configure(text="")
        show_dashboard()
    else:
        login_error.configure(text="Invalid student ID or password")

# ============ PAGES ============
def show_signup():
    global signup_vars, signup_subjects_text, terms_agreed
    clear_window()
    
    main = ctk.CTkFrame(root, fg_color="transparent")
    main.pack(fill="both", expand=True)
    
    hero = ctk.CTkFrame(main, fg_color=C["primary_dark"], width=550)
    hero.pack(side="left", fill="both")
    hero.pack_propagate(False)
    
    hc = ctk.CTkFrame(hero, fg_color="transparent")
    hc.pack(padx=60, pady=(80, 40), fill="both", expand=True)
    
    ctk.CTkLabel(hc, text="🎓", font=("Arial", 24), width=40, height=40,
                fg_color=C["gold"], corner_radius=10, text_color=C["primary_dark"]).pack(anchor="w")
    ctk.CTkLabel(hc, text="Limkokwing Student Portal", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w", pady=(10, 60))
    ctk.CTkLabel(hc, text="Join thousands\nof learners.", font=("Arial", 34, "bold"),
                text_color="white", justify="left").pack(anchor="w")
    ctk.CTkLabel(hc, text="Create your student account and get instant\naccess to courses, grades, assignments,\nand your personal learning dashboard.",
                font=("Arial", 13), text_color="#bfdbfe", justify="left").pack(anchor="w", pady=(15, 0))
    
    auth = ctk.CTkScrollableFrame(main, fg_color="transparent", width=550)
    auth.pack(side="right", fill="both", expand=True, padx=40, pady=40)
    
    card = ctk.CTkFrame(auth, fg_color="white", corner_radius=16)
    card.pack(fill="x", pady=(20, 0))
    
    ctk.CTkButton(card, text="‹ Back to sign in", fg_color="transparent", text_color=C["text_muted"],
                 font=("Arial", 12), hover=False, command=lambda: set_view("login")).pack(padx=25, pady=(25, 10), anchor="w")
    
    ctk.CTkLabel(card, text="Create your account", font=("Arial", 22, "bold"),
                text_color=C["text"]).pack(padx=30, anchor="w")
    ctk.CTkLabel(card, text="Fill in your details to register as a student",
                font=("Arial", 12), text_color=C["text_light"]).pack(padx=30, anchor="w", pady=(0, 20))
    
    signup_vars = {}
    
    for label_text, key, placeholder, show_char in [
        ("First Name *", "first_name", "Chris", ""),
        ("Last Name *", "last_name", "Effiong", ""),
        ("Email Address *", "email", "chris@school.edu", ""),
        ("Student ID (leave blank to auto-generate)", "student_id", "Auto-generated if empty", ""),
        ("Institution / School *", "institution", "Limkokwing College", ""),
        ("Password *", "password", "Min. 6 characters", "*"),
        ("Confirm Password *", "confirm_password", "Re-enter password", "*")
    ]:
        ctk.CTkLabel(card, text=label_text, font=("Arial", 12), text_color="#334155").pack(padx=30, anchor="w", pady=(8, 3))
        v = ctk.StringVar()
        signup_vars[key] = v
        entry = ctk.CTkEntry(card, textvariable=v, placeholder_text=placeholder, height=35, corner_radius=10, border_color=C["border"])
        if show_char:
            entry.configure(show=show_char)
        entry.pack(padx=30, fill="x")

        if key == "institution":
            ctk.CTkLabel(card, text="Your Subjects / Courses *", font=("Arial", 12), text_color="#334155").pack(padx=30, anchor="w", pady=(8, 3))
            ctk.CTkLabel(card, text="Type your subjects separated by comma or new line. Example: Programming, Database, Multimedia",
                         font=("Arial", 10), text_color=C["text_muted"], wraplength=430).pack(padx=30, anchor="w")
            signup_subjects_text = ctk.CTkTextbox(card, height=75, corner_radius=10, border_color=C["border"], border_width=1)
            signup_subjects_text.pack(padx=30, fill="x", pady=(4, 5))
    
    terms_agreed = ctk.BooleanVar(value=False)
    ctk.CTkCheckBox(card, text="I agree to the Terms of Service and Privacy Policy",
                   variable=terms_agreed).pack(padx=30, pady=10, anchor="w")
    
    ctk.CTkButton(card, text="Create Account", command=signup_submit,
                 fg_color=C["primary"], height=40, font=("Arial", 13, "bold"),
                 corner_radius=12).pack(padx=30, pady=15, fill="x")
    
    ctk.CTkButton(card, text="Already have an account? Sign in", fg_color="transparent",
                 text_color=C["blue"], font=("Arial", 11), hover=False,
                 command=lambda: set_view("login")).pack(pady=(0, 20))

def show_success():
    clear_window()
    main = ctk.CTkFrame(root, fg_color="transparent")
    main.pack(fill="both", expand=True)
    hero = ctk.CTkFrame(main, fg_color=C["primary_dark"], width=550)
    hero.pack(side="left", fill="both")
    hero.pack_propagate(False)
    hc = ctk.CTkFrame(hero, fg_color="transparent")
    hc.pack(padx=60, pady=80, fill="both", expand=True)
    ctk.CTkLabel(hc, text="🎓", font=("Arial", 24), width=40, height=40,
                fg_color=C["gold"], corner_radius=10, text_color=C["primary_dark"]).pack(anchor="w")
    ctk.CTkLabel(hc, text="Limkokwing Student Portal", font=("Arial", 18, "bold"), text_color="white").pack(anchor="w", pady=(10, 60))
    ctk.CTkLabel(hc, text="Welcome to\nthe community!", font=("Arial", 34, "bold"), text_color="white", justify="left").pack(anchor="w")
    ctk.CTkLabel(hc, text="Your account has been created.\nSign in to start learning.",
                font=("Arial", 13), text_color="#bfdbfe", justify="left").pack(anchor="w", pady=(15, 0))
    auth = ctk.CTkScrollableFrame(main, fg_color="transparent", width=550)
    auth.pack(side="right", fill="both", expand=True, padx=40, pady=40)
    card = ctk.CTkFrame(auth, fg_color="white", corner_radius=16)
    card.pack(fill="x", pady=(20, 0))
    ctk.CTkLabel(card, text="✅", font=("Arial", 50)).pack(pady=(40, 10))
    ctk.CTkLabel(card, text="Account Created!", font=("Arial", 22, "bold"), text_color=C["text"]).pack()
    ctk.CTkLabel(card, text="Your student account has been successfully\nregistered. You can now sign in.",
                font=("Arial", 12), text_color=C["text_light"], justify="center").pack(pady=10)
    ctk.CTkButton(card, text="Go to Sign In", command=lambda: set_view("login"),
                 fg_color=C["primary"], height=40, font=("Arial", 13, "bold"),
                 corner_radius=12).pack(padx=30, pady=20, fill="x")

def show_login():
    global login_id, login_pass, login_error, show_pw
    clear_window()
    if login_view == "signup":
        show_signup()
        return
    if login_view == "success":
        show_success()
        return
    
    main = ctk.CTkFrame(root, fg_color="transparent")
    main.pack(fill="both", expand=True)
    hero = ctk.CTkFrame(main, fg_color=C["primary_dark"], width=550)
    hero.pack(side="left", fill="both")
    hero.pack_propagate(False)
    hc = ctk.CTkFrame(hero, fg_color="transparent")
    hc.pack(padx=60, pady=(80, 40), fill="both", expand=True)
    
    brand = ctk.CTkFrame(hc, fg_color="transparent")
    brand.pack(anchor="w")
    ctk.CTkLabel(brand, text="🎓", font=("Arial", 24), width=40, height=40,
                fg_color=C["gold"], corner_radius=10, text_color=C["primary_dark"]).pack(side="left", padx=(0, 10))
    ctk.CTkLabel(brand, text="Limkokwing Student Portal", font=("Arial", 18, "bold"), text_color="white").pack(side="left")
    
    ctk.CTkLabel(hc, text="Your learning\njourney starts here.", font=("Arial", 34, "bold"),
                text_color="white", justify="left").pack(anchor="w", pady=(60, 15))
    ctk.CTkLabel(hc, text="Access your courses, track your progress, submit\nassignments, and stay on top of your academic goals\n— all in one place.",
                font=("Arial", 13), text_color="#bfdbfe", justify="left", wraplength=400).pack(anchor="w")
    
    sf = ctk.CTkFrame(hc, fg_color="transparent")
    sf.pack(side="bottom", fill="x")
    for val, lbl in [("4,200+", "Active Students"), ("180+", "Courses Available"), ("B+", "Avg. Grade")]:
        st = ctk.CTkFrame(sf, fg_color=C["stat_bg"], corner_radius=12)
        st.pack(side="left", padx=(0, 10), expand=True, fill="x")
        ctk.CTkLabel(st, text=val, font=("Arial", 20, "bold"), text_color=C["gold"]).pack(pady=(12, 0))
        ctk.CTkLabel(st, text=lbl, font=("Arial", 10), text_color="#bfdbfe").pack(pady=(0, 12))
    
    auth = ctk.CTkScrollableFrame(main, fg_color="transparent", width=550)
    auth.pack(side="right", fill="both", expand=True, padx=40, pady=40)
    card = ctk.CTkFrame(auth, fg_color="white", corner_radius=16)
    card.pack(fill="x", pady=(20, 0))
    
    ctk.CTkLabel(card, text="Student Sign In", font=("Arial", 22, "bold"),
                text_color=C["text"]).pack(padx=30, pady=(30, 5), anchor="w")
    ctk.CTkLabel(card, text="Enter your credentials to access your portal",
                font=("Arial", 12), text_color=C["text_light"]).pack(padx=30, anchor="w", pady=(0, 25))
    
    ctk.CTkLabel(card, text="Student ID", font=("Arial", 12, "bold"), text_color="#334155").pack(padx=30, anchor="w")
    id_frame = ctk.CTkFrame(card, fg_color="#f8fafc", corner_radius=12, border_width=1, border_color=C["border"])
    id_frame.pack(padx=30, fill="x", pady=(5, 15))
    ctk.CTkLabel(id_frame, text="#", font=("Arial", 14), text_color=C["text_muted"]).pack(side="left", padx=12)
    login_id = ctk.CTkEntry(id_frame, placeholder_text="905006734", fg_color="transparent",
                            border_width=0, height=38, font=("Arial", 13))
    login_id.pack(side="left", fill="x", expand=True, padx=(0, 10))
    
    ctk.CTkLabel(card, text="Password", font=("Arial", 12, "bold"), text_color="#334155").pack(padx=30, anchor="w")
    pw_frame = ctk.CTkFrame(card, fg_color="#f8fafc", corner_radius=12, border_width=1, border_color=C["border"])
    pw_frame.pack(padx=30, fill="x", pady=(5, 5))
    ctk.CTkLabel(pw_frame, text="🔒", font=("Arial", 14)).pack(side="left", padx=12)
    login_pass = ctk.CTkEntry(pw_frame, placeholder_text="Enter your password", show="*",
                              fg_color="transparent", border_width=0, height=38, font=("Arial", 13))
    login_pass.pack(side="left", fill="x", expand=True, padx=(0, 10))
    
    show_pw = ctk.BooleanVar(value=False)
    ctk.CTkCheckBox(card, text="Show password", variable=show_pw,
                   command=toggle_password).pack(padx=30, pady=(5, 5), anchor="w")
    
    login_error = ctk.CTkLabel(card, text="", font=("Arial", 11), text_color=C["red"])
    login_error.pack(padx=30, pady=5)
    
    ctk.CTkButton(card, text="Sign In", command=login,
                 fg_color=C["primary"], hover_color="#152d54",
                 height=42, font=("Arial", 14, "bold"), corner_radius=12).pack(padx=30, pady=15, fill="x")
    
    demo_frame = ctk.CTkFrame(card, fg_color="transparent")
    demo_frame.pack(padx=30, fill="x", pady=(10, 0))
    ctk.CTkLabel(demo_frame, text="DEMO ACCOUNTS", font=("Arial", 10, "bold"),
                text_color=C["text_muted"]).pack(anchor="w", pady=(0, 10))
    
    for s in STUDENTS[:3]:
        btn = ctk.CTkFrame(demo_frame, fg_color="transparent", height=40, cursor="hand2")
        btn.pack(fill="x", pady=2)
        btn.pack_propagate(False)
        ctk.CTkLabel(btn, text=s["avatar"], font=("Arial", 11, "bold"), width=30, height=30,
                    fg_color="#dbeafe", text_color=C["blue"], corner_radius=15).place(x=0, y=5)
        info = ctk.CTkFrame(btn, fg_color="transparent")
        info.place(x=42, y=2)
        ctk.CTkLabel(info, text=s["name"], font=("Arial", 12, "bold"), text_color="#334155").pack(anchor="w")
        ctk.CTkLabel(info, text=f"{s['id']} · {s['grade']}", font=("Arial", 9), text_color=C["text_muted"]).pack(anchor="w")
        def make_fill(s):
            return lambda e: fill_demo(s)
        btn.bind("<Button-1>", make_fill(s))
        for child in btn.winfo_children():
            child.bind("<Button-1>", make_fill(s))
            for sub in child.winfo_children():
                sub.bind("<Button-1>", make_fill(s))
    
    ctk.CTkButton(card, text="Don't have an account? Sign up", fg_color="transparent",
                 text_color=C["blue"], font=("Arial", 11, "underline"), hover=False,
                 command=lambda: set_view("signup")).pack(pady=20)

# ============ DASHBOARD ============
def navigate(page):
    global current_page, page_title
    current_page = page
    page_title.configure(text=page.capitalize())
    for pid, btn in nav_buttons.items():
        btn.configure(fg_color=C["primary_light"] if pid == page else "transparent",
                     font=("Arial", 12, "bold") if pid == page else ("Arial", 12))
    for w in page_container.winfo_children(): w.destroy()
    {"dashboard": render_dashboard, "courses": render_courses, "assignments": render_assignments,
     "grades": render_grades, "calendar": render_calendar, "messages": render_messages,
     "settings": render_settings}[page]()

def show_dashboard():
    global nav_buttons, page_container, page_title
    clear_window()
    user = current_user
    main = ctk.CTkFrame(root, fg_color="transparent")
    main.pack(fill="both", expand=True)
    start_particles(main)
    
    sidebar = ctk.CTkFrame(main, fg_color=C["sidebar"], width=220, corner_radius=0)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    
    logo = ctk.CTkFrame(sidebar, fg_color="transparent")
    logo.pack(padx=15, pady=18, fill="x")
    ctk.CTkLabel(logo, text="🎓", font=("Arial", 18), width=34, height=34,
                fg_color=C["gold"], corner_radius=8, text_color=C["primary_dark"]).pack(side="left", padx=(0, 8))
    ctk.CTkLabel(logo, text="Limkokwing", font=("Arial", 15, "bold"), text_color="white").pack(side="left")
    
    nav_items = [("dashboard", "📊 Dashboard"), ("courses", "📚 My Courses"), ("assignments", "📋 Assignments"),
                 ("grades", "📈 Grades"), ("calendar", "📅 Calendar"), ("messages", "💬 Messages")]
    nav_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
    nav_frame.pack(padx=10, pady=10, fill="x")
    
    nav_buttons = {}
    for pid, label in nav_items:
        is_active = pid == current_page
        btn = ctk.CTkButton(nav_frame, text=label, anchor="w",
                           fg_color=C["primary_light"] if is_active else "transparent",
                           hover_color=C["primary_light"], text_color="white",
                           font=("Arial", 12, "bold") if is_active else ("Arial", 12),
                           height=36, corner_radius=8, command=lambda p=pid: navigate(p))
        btn.pack(fill="x", pady=1)
        nav_buttons[pid] = btn
    
    sb = ctk.CTkFrame(sidebar, fg_color="transparent")
    sb.pack(side="bottom", padx=10, pady=12, fill="x")
    ctk.CTkButton(sb, text="⚙ Settings", anchor="w", fg_color="transparent", hover_color=C["primary_light"],
                 text_color="#bfdbfe", font=("Arial", 12), height=35, corner_radius=8,
                 command=lambda: navigate("settings")).pack(fill="x")
    ctk.CTkButton(sb, text="↩ Sign Out", anchor="w", fg_color="transparent", hover_color="#dc2626",
                 text_color="#bfdbfe", font=("Arial", 12), height=35, corner_radius=8,
                 command=show_login).pack(fill="x")
    
    uf = ctk.CTkFrame(sb, fg_color="#1e3354", corner_radius=10)
    uf.pack(fill="x", pady=(8, 0))
    ctk.CTkLabel(uf, text=user["avatar"], font=("Arial", 12, "bold"), width=30, height=30,
                fg_color=C["gold"], text_color=C["primary_dark"], corner_radius=15).pack(side="left", padx=10, pady=10)
    ui = ctk.CTkFrame(uf, fg_color="transparent")
    ui.pack(side="left", padx=(5, 10), pady=10)
    ctk.CTkLabel(ui, text=user["name"], font=("Arial", 11, "bold"), text_color="white").pack(anchor="w")
    ctk.CTkLabel(ui, text=user["grade"], font=("Arial", 9), text_color="#93c5fd").pack(anchor="w")
    
    content = ctk.CTkFrame(main, fg_color=C["bg"])
    content.pack(side="right", fill="both", expand=True)
    
    top_bar = ctk.CTkFrame(content, fg_color="white", height=56, corner_radius=0)
    top_bar.pack(fill="x")
    top_bar.pack_propagate(False)
    page_title = ctk.CTkLabel(top_bar, text="Dashboard", font=("Arial", 14), text_color=C["text_light"])
    page_title.pack(side="left", padx=20)
    ctk.CTkButton(top_bar, text="🔔", width=32, height=32, fg_color="transparent",
                 hover_color="#f1f5f9", text_color=C["text_light"]).pack(side="right", padx=5)
    ctk.CTkButton(top_bar, text=user["avatar"], width=32, height=32, corner_radius=16,
                 fg_color=C["gold"], text_color=C["primary_dark"], font=("Arial", 11, "bold"),
                 command=lambda: navigate("settings")).pack(side="right", padx=5)
    
    page_container = ctk.CTkFrame(content, fg_color=C["bg"])
    page_container.pack(fill="both", expand=True)
    render_dashboard()

# ============ ALL RENDER FUNCTIONS ============
def render_dashboard():
    user = current_user
    scroll = ctk.CTkScrollableFrame(page_container, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=24, pady=24)
    now = datetime.now()
    h = now.hour
    g = "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"
    
    ctk.CTkLabel(scroll, text=f"{g}, {user['name'].split()[0]}.", font=("Arial", 24, "bold"),
                text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(scroll, text=f"{now.strftime('%A, %B %d, %Y')} · {user['grade']}",
                font=("Arial", 12), text_color=C["text_light"]).pack(anchor="w", pady=(5, 20))
    
    courses = get_user_courses()
    assignments = get_user_assignments()
    pending_count = sum(1 for a in assignments if a.get("status") == "pending")
    avg_score = sum(c["score"] for c in courses) / len(courses)
    gpa = avg_score / 100 * 4

    sf = ctk.CTkFrame(scroll, fg_color="transparent"); sf.pack(fill="x")
    for icon, val, lab, sub, clr in [
        ("📈", f"{gpa:.1f}", "Current GPA", "Based on your subjects", C["primary"]),
        ("📚", str(len(courses)), "Active Courses", "Your selected subjects", C["amber"]),
        ("⏰", str(pending_count), "Pending Tasks", "From your subjects", C["red"]),
        ("✅", str(len([a for a in assignments if a.get("status") in ["submitted", "graded"]])), "Completed", "This semester", C["emerald"])]:
        card = ctk.CTkFrame(sf, fg_color="white", corner_radius=12)
        card.pack(side="left", padx=(0, 10), expand=True, fill="both")
        icf = ctk.CTkFrame(card, fg_color=clr, width=34, height=34, corner_radius=8)
        icf.pack(padx=16, pady=(16, 8), anchor="w"); icf.pack_propagate(False)
        ctk.CTkLabel(icf, text=icon, font=("Arial", 14), text_color="white").pack(expand=True)
        ctk.CTkLabel(card, text=val, font=("Arial", 22, "bold"), text_color=C["text"]).pack(padx=16, anchor="w")
        ctk.CTkLabel(card, text=lab, font=("Arial", 11), text_color=C["text_light"]).pack(padx=16, anchor="w")
        ctk.CTkLabel(card, text=sub, font=("Arial", 10), text_color=C["text_muted"]).pack(padx=16, pady=(2, 16), anchor="w")
    
    ctk.CTkFrame(scroll, height=20, fg_color="transparent").pack()
    
    ap = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); ap.pack(fill="x")
    ah = ctk.CTkFrame(ap, fg_color="transparent"); ah.pack(fill="x", padx=20, pady=(16, 8))
    ctk.CTkLabel(ah, text="Upcoming Assignments", font=("Arial", 15, "bold"), text_color=C["text"]).pack(side="left")
    ctk.CTkButton(ah, text="View all ›", fg_color="transparent", text_color=C["blue"],
                 font=("Arial", 11, "bold"), hover=False, command=lambda: navigate("assignments")).pack(side="right")
    for u in get_user_upcoming():
        rw = ctk.CTkFrame(ap, fg_color="transparent"); rw.pack(fill="x", padx=16, pady=2)
        ctk.CTkLabel(rw, text="⚠" if u["urg"] else "!", font=("Arial", 14),
                    text_color=C["red"] if u["urg"] else "#cbd5e1", width=24).pack(side="left")
        inf = ctk.CTkFrame(rw, fg_color="transparent"); inf.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(inf, text=u["task"], font=("Arial", 12, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(inf, text=u["subj"], font=("Arial", 10), text_color=C["text_muted"]).pack(anchor="w")
        ctk.CTkLabel(rw, text=u["due"], font=("Arial", 10, "bold"),
                    text_color=C["red"] if u["urg"] else C["text_light"],
                    fg_color="#fef2f2" if u["urg"] else "#f1f5f9", corner_radius=12, padx=8).pack(side="right")
    ctk.CTkFrame(ap, fg_color="transparent", height=8).pack()
    ctk.CTkFrame(scroll, height=20, fg_color="transparent").pack()
    
    rg = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); rg.pack(fill="x", pady=(0, 20))
    rh = ctk.CTkFrame(rg, fg_color="transparent"); rh.pack(fill="x", padx=20, pady=(16, 8))
    ctk.CTkLabel(rh, text="Recent Grades", font=("Arial", 15, "bold"), text_color=C["text"]).pack(side="left")
    ctk.CTkButton(rh, text="See all ›", fg_color="transparent", text_color=C["blue"],
                 font=("Arial", 11, "bold"), hover=False, command=lambda: navigate("grades")).pack(side="right")
    for a in [x for x in get_user_assignments() if x["status"] == "graded"][:3]:
        rw = ctk.CTkFrame(rg, fg_color="transparent"); rw.pack(fill="x", padx=16, pady=4)
        bg, fg = grade_color(a.get("grade", "C"))
        ctk.CTkLabel(rw, text=a.get("grade", "?"), font=("Arial", 10, "bold"),
                    fg_color=bg, text_color=fg, corner_radius=6, padx=8, pady=4).pack(side="left")
        inf = ctk.CTkFrame(rw, fg_color="transparent"); inf.pack(side="left", padx=8)
        ctk.CTkLabel(inf, text=a["title"], font=("Arial", 11, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(inf, text=f"{a['subj']} · {a.get('score', '')}", font=("Arial", 9), text_color=C["text_muted"]).pack(anchor="w")
    
    cp = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); cp.pack(fill="x")
    ch = ctk.CTkFrame(cp, fg_color="transparent"); ch.pack(fill="x", padx=20, pady=(16, 8))
    ctk.CTkLabel(ch, text="Course Progress", font=("Arial", 15, "bold"), text_color=C["text"]).pack(side="left")
    ctk.CTkButton(ch, text="All courses ›", fg_color="transparent", text_color=C["blue"],
                 font=("Arial", 11, "bold"), hover=False, command=lambda: navigate("courses")).pack(side="right")
    cg = ctk.CTkFrame(cp, fg_color="transparent"); cg.pack(padx=16, pady=(0, 16), fill="x")
    for i, c in enumerate(get_user_courses()[:4]):
        cf = ctk.CTkFrame(cg, fg_color="transparent")
        cf.pack(side="left", padx=(0, 16) if i < 3 else 0, expand=True, fill="x")
        ctk.CTkLabel(cf, text=c["name"], font=("Arial", 12, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(cf, text=c["teacher"], font=("Arial", 10), text_color=C["text_muted"]).pack(anchor="w", pady=(2, 8))
        pb = ctk.CTkProgressBar(cf, height=6, progress_color=c["color"], fg_color="#e2e8f0", corner_radius=3)
        pb.pack(fill="x"); pb.set(c["progress"] / 100)
        ctk.CTkLabel(cf, text=f"{c['progress']}% complete", font=("Arial", 10), text_color=C["text_light"]).pack(anchor="w", pady=(4, 0))
    ctk.CTkFrame(scroll, height=30, fg_color="transparent").pack()

def render_courses():
    scroll = ctk.CTkScrollableFrame(page_container, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=24, pady=24)
    ctk.CTkLabel(scroll, text="My Courses", font=("Arial", 26, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(scroll, text=f"Spring Semester 2025 · {len(get_user_courses())} enrolled courses", font=("Arial", 12),
                text_color=C["text_light"]).pack(anchor="w", pady=(5, 20))
    grid = ctk.CTkFrame(scroll, fg_color="transparent"); grid.pack(fill="x")
    rf = None
    for i, c in enumerate(get_user_courses()):
        if i % 3 == 0: rf = ctk.CTkFrame(grid, fg_color="transparent"); rf.pack(fill="x", pady=(0, 15))
        card = ctk.CTkFrame(rf, fg_color="white", corner_radius=12)
        card.pack(side="left", padx=(0, 12) if (i % 3) < 2 else 0, expand=True, fill="x")
        hdr = ctk.CTkFrame(card, fg_color=c["color"], height=80, corner_radius=12)
        hdr.pack(fill="x"); hdr.pack_propagate(False)
        ctk.CTkLabel(hdr, text=c["code"], font=("Arial", 10), text_color="white").pack(padx=15, pady=(15, 0), anchor="w")
        ctk.CTkLabel(hdr, text=c["name"], font=("Arial", 14, "bold"), text_color="white").pack(padx=15, anchor="w")
        bd = ctk.CTkFrame(card, fg_color="transparent"); bd.pack(padx=15, pady=12, fill="x")
        ctk.CTkLabel(bd, text=c["teacher"], font=("Arial", 11, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(bd, text=f"👥 {c['students']} students  ·  ★ {c['score']}/100",
                    font=("Arial", 10), text_color=C["text_muted"]).pack(anchor="w", pady=(2, 8))
        pb = ctk.CTkProgressBar(bd, height=6, progress_color=c["color"], fg_color="#e2e8f0", corner_radius=3)
        pb.pack(fill="x"); pb.set(c["progress"] / 100)
        nf = ctk.CTkFrame(bd, fg_color="#f8fafc", corner_radius=8); nf.pack(fill="x", pady=(8, 0))
        ctk.CTkLabel(nf, text="Next topic", font=("Arial", 9), text_color=C["text_muted"]).pack(padx=10, pady=(8, 0), anchor="w")
        ctk.CTkLabel(nf, text=c["next"], font=("Arial", 11, "bold"), text_color=C["text"]).pack(padx=10, pady=(0, 8), anchor="w")
    ctk.CTkFrame(scroll, height=30, fg_color="transparent").pack()

# ============ ASSIGNMENTS (FIXED) ============
def render_assignments():
    global assignments_container, filter_var, filter_buttons
    scroll = ctk.CTkScrollableFrame(page_container, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=24, pady=24)
    ctk.CTkLabel(scroll, text="Assignments", font=("Arial", 26, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(scroll, text="Spring Semester 2025", font=("Arial", 12), text_color=C["text_light"]).pack(anchor="w", pady=(5, 20))
    
    filter_frame = ctk.CTkFrame(scroll, fg_color="transparent")
    filter_frame.pack(anchor="w", pady=(0, 15))
    
    filter_buttons = {}
    filter_var = "all"
    
    counts = {
        "all": len(get_user_assignments()),
        "pending": sum(1 for a in get_user_assignments() if a["status"] == "pending"),
        "submitted": sum(1 for a in get_user_assignments() if a["status"] == "submitted"),
        "graded": sum(1 for a in get_user_assignments() if a["status"] == "graded")
    }
    
    tab_colors = {
        "all": C["primary"],
        "pending": "#f59e0b",
        "submitted": "#3b82f6",
        "graded": "#10b981"
    }
    
    for f in ["all", "pending", "submitted", "graded"]:
        is_active = filter_var == f
        btn = ctk.CTkButton(
            filter_frame, 
            text=f"{f.capitalize()} ({counts[f]})",
            font=("Arial", 11, "bold"),
            fg_color=tab_colors[f] if is_active else "white",
            text_color="white" if is_active else C["text_light"],
            border_color=C["border"] if not is_active else None,
            border_width=1 if not is_active else 0,
            hover_color=tab_colors[f],
            height=32,
            corner_radius=8,
            command=lambda fv=f: filter_assignments(fv)
        )
        btn.pack(side="left", padx=(0, 6))
        filter_buttons[f] = btn
    
    assignments_container = ctk.CTkFrame(scroll, fg_color="transparent")
    assignments_container.pack(fill="both", expand=True)
    render_assignment_list()

def filter_assignments(filter_type):
    global filter_var
    filter_var = filter_type
    
    tab_colors = {
        "all": C["primary"],
        "pending": "#f59e0b",
        "submitted": "#3b82f6",
        "graded": "#10b981"
    }
    
    for f, btn in filter_buttons.items():
        is_active = f == filter_type
        if is_active:
            btn.configure(fg_color=tab_colors[f], text_color="white", border_width=0)
        else:
            btn.configure(fg_color="white", text_color=C["text_light"], border_color=C["border"], border_width=1)
    
    render_assignment_list()

def render_assignment_list():
    for w in assignments_container.winfo_children():
        w.destroy()
    
    sc = {
        "pending": ("#fff7ed", "#ea580c", "⏳"),
        "submitted": ("#eff6ff", "#2563eb", "📤"),
        "graded": ("#f0fdf4", "#059669", "✅")
    }
    
    # Filter assignments properly
    filtered = []
    for a in get_user_assignments():
        status = "submitted" if a["id"] in submitted_assignments else a["status"]
        if filter_var == "all" or status == filter_var:
            filtered.append(a)
    
    if not filtered:
        empty = ctk.CTkFrame(assignments_container, fg_color="white", corner_radius=12, height=200)
        empty.pack(fill="x")
        empty.pack_propagate(False)
        ctk.CTkLabel(empty, text="📭", font=("Arial", 40)).pack(pady=(50, 10))
        ctk.CTkLabel(empty, text=f"No {filter_var} assignments", font=("Arial", 14), text_color=C["text_light"]).pack()
        return
    
    for a in filtered:
        status = "submitted" if a["id"] in submitted_assignments else a["status"]
        bg, fg, icon = sc.get(status, ("#f1f5f9", "#64748b", "📌"))
        
        card = ctk.CTkFrame(assignments_container, fg_color="white", corner_radius=12)
        card.pack(fill="x", pady=4)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=20, pady=15)
        
        left = ctk.CTkFrame(content, fg_color="transparent")
        left.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(left, text=a["subj"], font=("Arial", 10, "bold"), text_color=C["text_muted"]).pack(anchor="w")
        
        title_row = ctk.CTkFrame(left, fg_color="transparent")
        title_row.pack(fill="x", pady=(3, 5))
        if a.get("urg") and status == "pending":
            ctk.CTkLabel(title_row, text="⚠️", font=("Arial", 12), text_color=C["red"]).pack(side="left", padx=(0, 5))
        ctk.CTkLabel(title_row, text=a["title"], font=("Arial", 14, "bold"), text_color=C["text"]).pack(side="left")
        
        meta = ctk.CTkFrame(left, fg_color="transparent")
        meta.pack(fill="x", pady=(8, 0))
        ctk.CTkLabel(meta, text=f"📅 Due: {a['due']}", font=("Arial", 10), text_color=C["text_muted"]).pack(side="left")
        ctk.CTkLabel(meta, text=f"  📊 {a['pts']} pts", font=("Arial", 10), text_color=C["text_muted"]).pack(side="left", padx=15)
        
        if status == "graded":
            ctk.CTkLabel(meta, text=f"  🎯 {a.get('grade', '')} · {a.get('score', '')}", font=("Arial", 10, "bold"), text_color=C["green"]).pack(side="left", padx=15)
        
        right = ctk.CTkFrame(content, fg_color="transparent")
        right.pack(side="right")
        
        status_badge = ctk.CTkFrame(right, fg_color=bg, corner_radius=8)
        status_badge.pack(pady=(0, 8))
        ctk.CTkLabel(status_badge, text=f"{icon} {status.upper()}", font=("Arial", 10, "bold"), text_color=fg, padx=10, pady=3).pack()
        
        if status == "pending":
            ctk.CTkButton(right, text="📤 Submit", fg_color=C["primary"], font=("Arial", 11, "bold"),
                         height=30, corner_radius=8, command=lambda a=a: submit_assignment(a)).pack()

def submit_assignment(a):
    dialog = ctk.CTkToplevel(root); dialog.title("Submit Assignment"); dialog.geometry("500x400")
    dialog.configure(fg_color="white"); dialog.grab_set()
    ctk.CTkLabel(dialog, text="Submit Assignment", font=("Arial", 20, "bold"), text_color=C["text"]).pack(padx=30, pady=(30, 5), anchor="w")
    ctk.CTkLabel(dialog, text=a["title"], font=("Arial", 12), text_color=C["text_light"]).pack(padx=30, anchor="w")
    ctk.CTkFrame(dialog, height=2, fg_color=C["border"]).pack(fill="x", padx=30, pady=15)
    ctk.CTkLabel(dialog, text="Attachment", font=("Arial", 12, "bold"), text_color=C["text"]).pack(padx=30, anchor="w")
    file_frame = ctk.CTkFrame(dialog, fg_color="#f8fafc", corner_radius=10); file_frame.pack(fill="x", padx=30, pady=(5, 15))
    global file_var
    file_var = ctk.StringVar(value="No file selected")
    ctk.CTkLabel(file_frame, textvariable=file_var, font=("Arial", 11), text_color=C["text_muted"]).pack(side="left", padx=12, pady=10)
    ctk.CTkButton(file_frame, text="Browse", font=("Arial", 11), fg_color=C["primary"], hover_color=C["primary_light"],
                 height=30, width=80, corner_radius=8, command=browse_file).pack(side="right", padx=10)
    global note_text
    ctk.CTkLabel(dialog, text="Note (optional)", font=("Arial", 12, "bold"), text_color=C["text"]).pack(padx=30, anchor="w")
    note_text = ctk.CTkTextbox(dialog, height=80, corner_radius=10, border_color=C["border"], border_width=1)
    note_text.pack(fill="x", padx=30, pady=(5, 15))
    btn_frame = ctk.CTkFrame(dialog, fg_color="transparent"); btn_frame.pack(fill="x", padx=30, pady=(0, 25))
    ctk.CTkButton(btn_frame, text="Cancel", font=("Arial", 12), fg_color="#f1f5f9", text_color=C["text_light"],
                 hover_color="#e2e8f0", height=35, corner_radius=8, command=dialog.destroy).pack(side="left", padx=(0, 10))
    ctk.CTkButton(btn_frame, text="Submit", font=("Arial", 12, "bold"), fg_color=C["primary"],
                 hover_color=C["primary_light"], height=35, corner_radius=8, expand=True,
                 command=lambda: confirm_submit(a, dialog)).pack(side="left", expand=True)

def browse_file():
    filename = filedialog.askopenfilename()
    if filename: file_var.set(filename.split("/")[-1])

def confirm_submit(a, dialog):
    submitted_assignments.add(a["id"]); dialog.destroy()
    messagebox.showinfo("Submitted", f'"{a["title"]}" submitted successfully!')
    render_assignment_list()

def render_grades():
    scroll = ctk.CTkScrollableFrame(page_container, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=24, pady=24)
    ctk.CTkLabel(scroll, text="Grades & Performance", font=("Arial", 26, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(scroll, text="Spring Semester 2025", font=("Arial", 12), text_color=C["text_light"]).pack(anchor="w", pady=(5, 20))
    courses = get_user_courses()
    avg_score = sum(c["score"] for c in courses) / len(courses)
    gpa = avg_score / 100 * 4
    gf = ctk.CTkFrame(scroll, fg_color="transparent"); gf.pack(fill="x", pady=(0, 20))
    for lb, vl, sb in [(f"Cumulative GPA", f"{gpa:.2f}", "Out of 4.0"),
                       (f"Average Score", f"{avg_score:.0f}%", "Across all courses"),
                       ("Class Rank", "#12", "Out of 28 students")]:
        card = ctk.CTkFrame(gf, fg_color="white", corner_radius=12)
        card.pack(side="left", padx=(0, 10), expand=True, fill="x")
        ctk.CTkLabel(card, text=lb, font=("Arial", 10), text_color=C["text_muted"]).pack(padx=16, pady=(16, 5), anchor="w")
        ctk.CTkLabel(card, text=vl, font=("Arial", 26, "bold"), text_color=C["text"]).pack(padx=16, anchor="w")
        ctk.CTkLabel(card, text=sb, font=("Arial", 10), text_color=C["text_muted"]).pack(padx=16, pady=(0, 16), anchor="w")
    chart_frame = ctk.CTkFrame(scroll, fg_color="transparent"); chart_frame.pack(fill="x", pady=(0, 20))
    bar_card = ctk.CTkFrame(chart_frame, fg_color="white", corner_radius=12)
    bar_card.pack(side="left", expand=True, fill="both", padx=(0, 10))
    ctk.CTkLabel(bar_card, text="Score by Subject", font=("Arial", 14, "bold"), text_color=C["text"]).pack(padx=16, pady=(12, 8), anchor="w")
    fig1 = Figure(figsize=(4.5, 2.8), dpi=90, facecolor="white")
    ax1 = fig1.add_subplot(111)
    ax1.bar([c["name"].split()[0] for c in courses], [c["score"] for c in courses], color=C["primary"], width=0.5)
    ax1.set_ylim(60, 100); ax1.set_facecolor("white"); ax1.tick_params(labelsize=7)
    fig1.tight_layout()
    FigureCanvasTkAgg(fig1, bar_card).get_tk_widget().pack(padx=10, pady=(0, 12), fill="both", expand=True)
    line_card = ctk.CTkFrame(chart_frame, fg_color="white", corner_radius=12)
    line_card.pack(side="left", expand=True, fill="both")
    ctk.CTkLabel(line_card, text="Score Trend", font=("Arial", 14, "bold"), text_color=C["text"]).pack(padx=16, pady=(12, 8), anchor="w")
    fig2 = Figure(figsize=(3.5, 2.8), dpi=90, facecolor="white")
    ax2 = fig2.add_subplot(111)
    score_trend = get_user_score_trend()
    ax2.plot(range(1, len(score_trend)+1), score_trend, color=C["gold"], linewidth=2, marker="o", markersize=5)
    ax2.set_ylim(70, 100); ax2.set_facecolor("white"); ax2.tick_params(labelsize=7)
    fig2.tight_layout()
    FigureCanvasTkAgg(fig2, line_card).get_tk_widget().pack(padx=10, pady=(0, 12), fill="both", expand=True)
    pn = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); pn.pack(fill="x")
    ctk.CTkLabel(pn, text="Course Grades", font=("Arial", 15, "bold"), text_color=C["text"]).pack(padx=20, pady=(16, 10), anchor="w")
    for c in courses:
        rw = ctk.CTkFrame(pn, fg_color="transparent"); rw.pack(fill="x", padx=16, pady=2)
        ctk.CTkLabel(rw, text=c["name"], font=("Arial", 12, "bold"), text_color=C["text"], width=180, anchor="w").pack(side="left")
        ctk.CTkLabel(rw, text=c["code"], font=("Arial", 10), text_color=C["text_muted"], width=90).pack(side="left")
        bg, fg = grade_color(c["grade"])
        ctk.CTkLabel(rw, text=c["grade"], font=("Arial", 11, "bold"), text_color=fg, fg_color=bg, corner_radius=6, padx=10).pack(side="left", padx=10)
        ctk.CTkLabel(rw, text=f"{c['score']}%", font=("Arial", 12, "bold"), text_color=C["text"], width=60).pack(side="left")
        pb = ctk.CTkProgressBar(rw, height=6, progress_color=C["primary"], fg_color="#e2e8f0", corner_radius=3)
        pb.pack(side="left", fill="x", expand=True, padx=10); pb.set(c["score"] / 100)
    ctk.CTkFrame(scroll, height=30, fg_color="transparent").pack()

def render_calendar():
    for w in page_container.winfo_children(): w.destroy()
    top = ctk.CTkFrame(page_container, fg_color="transparent"); top.pack(fill="x", padx=24, pady=(24, 0))
    ctk.CTkLabel(top, text="Calendar", font=("Arial", 26, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(top, text="Upcoming deadlines and events", font=("Arial", 12), text_color=C["text_light"]).pack(anchor="w", pady=(5, 0))
    main = ctk.CTkFrame(page_container, fg_color="transparent"); main.pack(fill="both", expand=True, padx=24, pady=20)
    cal_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
    cal_card.pack(side="left", fill="both", expand=True, padx=(0, 10))
    nav = ctk.CTkFrame(cal_card, fg_color="transparent"); nav.pack(fill="x", padx=16, pady=(14, 8))
    ctk.CTkLabel(nav, text=f"{cal.month_name[cal_mo]} {cal_yr}", font=("Arial", 16, "bold"), text_color=C["text"]).pack(side="left")
    ctk.CTkButton(nav, text="◀", width=30, height=30, fg_color="transparent", text_color=C["text_light"],
                 hover_color="#f1f5f9", command=cal_prev).pack(side="right", padx=2)
    ctk.CTkButton(nav, text="▶", width=30, height=30, fg_color="transparent", text_color=C["text_light"],
                 hover_color="#f1f5f9", command=cal_next).pack(side="right", padx=2)
    dh = ctk.CTkFrame(cal_card, fg_color="transparent"); dh.pack(fill="x", padx=12)
    for day in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
        ctk.CTkLabel(dh, text=day, font=("Arial", 10, "bold"), text_color=C["text_muted"], width=80).pack(side="left")
    cgrid = cal.monthcalendar(cal_yr, cal_mo)
    today = datetime.now()
    gf2 = ctk.CTkFrame(cal_card, fg_color="transparent"); gf2.pack(fill="both", expand=True, padx=10, pady=5)
    for week in cgrid:
        rw = ctk.CTkFrame(gf2, fg_color="transparent"); rw.pack(fill="x", pady=1)
        for day in week:
            if day == 0: ctk.CTkFrame(rw, fg_color="transparent", width=80, height=55).pack(side="left", padx=1); continue
            user_events = get_user_events()
            hev = (cal_yr, cal_mo, day) in user_events
            itd = (today.year == cal_yr and today.month == cal_mo and today.day == day)
            cell_bg = "#dbeafe" if itd else ("#f0fdf4" if hev else "white")
            border = C["border"] if hev else ("#dbeafe" if itd else "white")
            cl = ctk.CTkFrame(rw, fg_color=cell_bg, width=80, height=55, corner_radius=6, border_width=1, border_color=border)
            cl.pack(side="left", padx=1); cl.pack_propagate(False)
            ctk.CTkLabel(cl, text=str(day), font=("Arial", 10, "bold" if itd else "normal"),
                        text_color=C["primary"] if itd else C["text"]).pack(anchor="nw", padx=4, pady=2)
            if hev: ctk.CTkLabel(cl, text=user_events[(cal_yr, cal_mo, day)][0][:12], font=("Arial", 7), text_color=C["green"]).pack(anchor="w", padx=4)
    ev_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12, width=250)
    ev_card.pack(side="right", fill="y"); ev_card.pack_propagate(False)
    ctk.CTkLabel(ev_card, text="Upcoming Events", font=("Arial", 14, "bold"), text_color=C["text"]).pack(padx=16, pady=(14, 10), anchor="w")
    evs = ctk.CTkScrollableFrame(ev_card, fg_color="transparent"); evs.pack(fill="both", expand=True, padx=10, pady=(0, 10))
    for (y, m, d), ev_list in sorted(get_user_events().items()):
        for e in ev_list:
            rw2 = ctk.CTkFrame(evs, fg_color="transparent"); rw2.pack(fill="x", pady=3)
            bar_c = C["red"] if "Exam" in e or "Finals" in e else C["green"]
            ctk.CTkFrame(rw2, width=4, height=28, fg_color=bar_c, corner_radius=2).pack(side="left", padx=(0, 8))
            inf = ctk.CTkFrame(rw2, fg_color="transparent"); inf.pack(side="left")
            ctk.CTkLabel(inf, text=e, font=("Arial", 11, "bold"), text_color=C["text"]).pack(anchor="w")
            ctk.CTkLabel(inf, text=f"{cal.month_abbr[m]} {d}, {y}", font=("Arial", 9), text_color=C["text_muted"]).pack(anchor="w")

def cal_prev():
    global cal_mo, cal_yr
    cal_mo -= 1
    if cal_mo < 1: cal_mo = 12; cal_yr -= 1
    render_calendar()

def cal_next():
    global cal_mo, cal_yr
    cal_mo += 1
    if cal_mo > 12: cal_mo = 1; cal_yr += 1
    render_calendar()

def render_messages():
    global active_conv, conversations, chat_container
    for w in page_container.winfo_children(): w.destroy()
    header = ctk.CTkFrame(page_container, fg_color="white", height=60); header.pack(fill="x"); header.pack_propagate(False)
    ctk.CTkLabel(header, text="Messages", font=("Arial", 24, "bold"), text_color=C["text"]).pack(side="left", padx=20)
    body = ctk.CTkFrame(page_container, fg_color="transparent"); body.pack(fill="both", expand=True)
    conv_list = ctk.CTkScrollableFrame(body, fg_color="white", width=250)
    conv_list.pack(side="left", fill="y"); conv_list.pack_propagate(False)
    active_conv = ctk.StringVar(value="1")
    conversations = get_user_conversations()
    for conv in conversations:
        is_active = active_conv.get() == str(conv["id"])
        btn = ctk.CTkFrame(conv_list, fg_color="#eff6ff" if is_active else "transparent", height=70, cursor="hand2")
        btn.pack(fill="x"); btn.pack_propagate(False)
        ctk.CTkLabel(btn, text=conv["av"], font=("Arial", 12, "bold"), width=35, height=35,
                    fg_color="#dbeafe", text_color=C["blue"], corner_radius=17).place(x=12, y=17)
        info = ctk.CTkFrame(btn, fg_color="transparent"); info.place(x=55, y=12)
        ctk.CTkLabel(info, text=conv["name"], font=("Arial", 12, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(info, text=conv["last"][:35] + ("..." if len(conv["last"]) > 35 else ""), font=("Arial", 10), text_color=C["text_muted"]).pack(anchor="w")
        if conv["unread"] > 0:
            ctk.CTkLabel(btn, text=str(conv["unread"]), font=("Arial", 10, "bold"), width=20, height=20,
                        fg_color=C["gold"], text_color=C["primary_dark"], corner_radius=10).place(x=210, y=25)
        btn.bind("<Button-1>", lambda e, cid=str(conv["id"]): select_conversation(cid))
    chat_container = ctk.CTkFrame(body, fg_color="white"); chat_container.pack(side="right", fill="both", expand=True)
    render_chat()

def select_conversation(conv_id):
    global active_conv, conversations
    active_conv.set(conv_id)
    for conv in conversations:
        if str(conv["id"]) == conv_id: conv["unread"] = 0; break
    for w in chat_container.winfo_children(): w.destroy()
    render_chat()

def render_chat():
    active = next((c for c in conversations if str(c["id"]) == active_conv.get()), conversations[0])
    ch = ctk.CTkFrame(chat_container, fg_color="#f8fafc", height=55); ch.pack(fill="x"); ch.pack_propagate(False)
    ctk.CTkLabel(ch, text=active["av"], font=("Arial", 11, "bold"), width=30, height=30,
                fg_color="#dbeafe", text_color=C["blue"], corner_radius=15).pack(side="left", padx=15)
    ci = ctk.CTkFrame(ch, fg_color="transparent"); ci.pack(side="left")
    ctk.CTkLabel(ci, text=active["name"], font=("Arial", 13, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(ci, text=active["role"], font=("Arial", 10), text_color=C["text_muted"]).pack(anchor="w")
    ms = ctk.CTkScrollableFrame(chat_container, fg_color="transparent"); ms.pack(fill="both", expand=True, padx=20, pady=15)
    for msg in active["msgs"]:
        is_me = msg["f"] == "me"
        bub = ctk.CTkFrame(ms, fg_color=C["primary"] if is_me else "#f1f5f9", corner_radius=12)
        bub.pack(anchor="e" if is_me else "w", pady=5)
        ctk.CTkLabel(bub, text=msg["t"], font=("Arial", 12), text_color="white" if is_me else C["text"], wraplength=300).pack(padx=12, pady=10)
        ctk.CTkLabel(ms, text=msg["tm"], font=("Arial", 9), text_color=C["text_muted"]).pack(anchor="e" if is_me else "w", pady=(0, 8))
    ipf = ctk.CTkFrame(chat_container, fg_color="#f8fafc", height=55); ipf.pack(fill="x", side="bottom"); ipf.pack_propagate(False)
    global msg_var
    msg_var = ctk.StringVar()
    msg_entry = ctk.CTkEntry(ipf, placeholder_text="Type a message…", height=35, corner_radius=10, border_color=C["border"], textvariable=msg_var)
    msg_entry.pack(side="left", padx=15, fill="x", expand=True)
    msg_entry.bind("<Return>", lambda e: send_message(ms, active))
    ctk.CTkButton(ipf, text="➤", width=40, height=35, corner_radius=10, fg_color=C["primary"],
                 command=lambda: send_message(ms, active)).pack(side="right", padx=15)

def send_message(ms_container, conv):
    text = msg_var.get().strip()
    if text:
        conv["msgs"].append({"f": "me", "t": text, "tm": "Just now"})
        conv["last"] = text; msg_var.set("")
        for w in chat_container.winfo_children(): w.destroy()
        render_chat()

def render_settings():
    global settings_vars, notif_vars, save_lbl
    user = current_user
    scroll = ctk.CTkScrollableFrame(page_container, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=24, pady=24)
    ctk.CTkLabel(scroll, text="Settings", font=("Arial", 26, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(scroll, text="Manage your account and preferences", font=("Arial", 12), text_color=C["text_light"]).pack(anchor="w", pady=(5, 20))
    profile = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); profile.pack(fill="x", pady=(0, 15))
    ctk.CTkLabel(profile, text="Profile", font=("Arial", 15, "bold"), text_color=C["text"]).pack(padx=20, pady=(16, 10), anchor="w")
    ar = ctk.CTkFrame(profile, fg_color="transparent"); ar.pack(padx=20, fill="x", pady=(0, 15))
    ctk.CTkLabel(ar, text=user["avatar"], font=("Arial", 20, "bold"), width=60, height=60,
                fg_color=C["primary"], text_color="white", corner_radius=12).pack(side="left")
    ai = ctk.CTkFrame(ar, fg_color="transparent"); ai.pack(side="left", padx=15)
    ctk.CTkLabel(ai, text=user["name"], font=("Arial", 14, "bold"), text_color=C["text"]).pack(anchor="w")
    ctk.CTkLabel(ai, text=f"{user['id']} · {user['grade']}", font=("Arial", 11), text_color=C["text_muted"]).pack(anchor="w")
    settings_vars = {}
    for lb, vl, dis in [("Full Name", user["name"], False), ("Email", "chris@school.edu", False), ("Student ID", user["id"], True)]:
        ctk.CTkLabel(profile, text=lb, font=("Arial", 12), text_color="#334155").pack(padx=20, anchor="w", pady=(5, 3))
        var = ctk.StringVar(value=vl)
        settings_vars[lb] = var
        en = ctk.CTkEntry(profile, height=35, corner_radius=10, border_color=C["border"], textvariable=var)
        if dis: en.configure(state="disabled", fg_color="#e2e8f0")
        en.pack(padx=20, fill="x", pady=(0, 10))
    notif = ctk.CTkFrame(scroll, fg_color="white", corner_radius=12); notif.pack(fill="x", pady=(0, 15))
    ctk.CTkLabel(notif, text="Notifications", font=("Arial", 15, "bold"), text_color=C["text"]).pack(padx=20, pady=(16, 10), anchor="w")
    notif_vars = {}
    for item, default in [("Assignment reminders", True), ("Grade updates", True), ("New messages", True), ("System alerts", False)]:
        f = ctk.CTkFrame(notif, fg_color="transparent"); f.pack(fill="x", padx=20, pady=4)
        var = ctk.BooleanVar(value=default)
        notif_vars[item] = var
        ctk.CTkCheckBox(f, text=item, variable=var, font=("Arial", 11)).pack(side="left")
    save_lbl = ctk.CTkLabel(scroll, text="", font=("Arial", 11), text_color=C["green"]); save_lbl.pack(anchor="w", pady=(0, 10))
    ctk.CTkButton(scroll, text="Save Changes", command=save_settings, fg_color=C["primary"], height=40,
                 font=("Arial", 13, "bold"), corner_radius=12).pack(fill="x")
    ctk.CTkFrame(scroll, height=30, fg_color="transparent").pack()

def save_settings():
    save_lbl.configure(text="✓ Changes saved successfully!")
    root.after(2500, lambda: save_lbl.configure(text=""))

# ============ RUN ============
def run():
    global root
    load_students()
    root = ctk.CTk()
    root.title("Limkokwing Student Portal")
    root.geometry("1200x750")
    root.minsize(900, 600)
    show_login()
    root.mainloop()

if __name__ == "__main__":
    run()