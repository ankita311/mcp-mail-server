import os
import smtplib
from email.message import EmailMessage
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP()

MAIL_ACCOUNT = os.getenv("MAIL_ACCOUNT")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")

@mcp.tool(name="send_email", description="Send an email using SMTP")
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email using SMTP."""
    try:
        msg = EmailMessage()
        msg['From'] = MAIL_ACCOUNT
        msg['To'] = to
        msg['Subject'] = subject
        msg.set_content(body)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(MAIL_ACCOUNT, MAIL_PASSWORD)
            server.send_message(msg)

        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
    
if __name__ == "__main__":
    mcp.run(transport='stdio')
