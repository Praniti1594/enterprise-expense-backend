const BASE_URL = "http://127.0.0.1:8000";

// ---------- AUTH ----------
function authHeaders() {
  return {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${localStorage.getItem("token")}`
  };
}

// ---------- LOGIN ----------
async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();

  if (res.ok) {
    localStorage.setItem("token", data.access_token);
    const payload = JSON.parse(atob(data.access_token.split(".")[1]));
    localStorage.setItem("role", payload.role);
    window.location.href = "dashboard.html";
  } else {
    output(data);
  }
}

// ---------- GUARD ----------
function checkAuth() {
  if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
  }
}

// ---------- DASHBOARD SETUP ----------
function setupDashboard() {
  const role = localStorage.getItem("role");

  if (role === "EMPLOYEE")
    document.getElementById("employee-actions").style.display = "block";

  if (role === "MANAGER")
    document.getElementById("manager-actions").style.display = "block";

  if (role === "ADMIN")
    document.getElementById("admin-actions").style.display = "block";
}

// ---------- LOGOUT ----------
function logout() {
  localStorage.clear();
  window.location.href = "login.html";
}

// ---------- EMPLOYEE ----------
async function addExpense() {
  const body = {
    category: document.getElementById("category").value,
    amount: document.getElementById("amount").value,
    expense_date: document.getElementById("date").value,
    receipt_url: "demo-url"
  };

  const res = await fetch(`${BASE_URL}/expenses`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(body)
  });

  output(await res.json());
}

// ---------- MANAGER & ADMIN ----------
async function approveExpense(role) {
  const expenseId =
    role === "MANAGER"
      ? document.getElementById("expenseIdManager").value
      : document.getElementById("expenseIdAdmin").value;

  const res = await fetch(
    `${BASE_URL}/approvals/expenses/${expenseId}/approve`,
    {
      method: "POST",
      headers: authHeaders(),
      body: JSON.stringify({ decision: "APPROVED" })
    }
  );

  output(await res.json());
}

async function rejectExpense(role) {
  const expenseId = document.getElementById("expenseIdManager").value;

  const res = await fetch(
    `${BASE_URL}/approvals/expenses/${expenseId}/approve`,
    {
      method: "POST",
      headers: authHeaders(),
      body: JSON.stringify({ decision: "REJECTED" })
    }
  );

  output(await res.json());
}

// ---------- ADMIN ----------
async function createPolicy() {
  const body = {
    category: document.getElementById("policyCategory").value,
    max_amount: document.getElementById("maxAmount").value,
    max_claims: document.getElementById("maxClaims").value,
    time_window: document.getElementById("timeWindow").value
  };

  const res = await fetch(`${BASE_URL}/policies`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(body)
  });

  output(await res.json());
}

// ---------- ANALYTICS ----------
async function getTeamSummary() {
  const res = await fetch(`${BASE_URL}/analytics/team-summary`, {
    headers: authHeaders()
  });
  output(await res.json());
}

async function getMonthlyTrend() {
  const res = await fetch(`${BASE_URL}/analytics/monthly-trend`, {
    headers: authHeaders()
  });
  output(await res.json());
}

async function getViolationRate() {
  const res = await fetch(`${BASE_URL}/analytics/violation-rate`, {
    headers: authHeaders()
  });
  output(await res.json());
}

// ---------- OUTPUT ----------
function output(data) {
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}

// ---------- INIT ----------
if (window.location.pathname.includes("dashboard.html")) {
  checkAuth();
  setupDashboard();
}
