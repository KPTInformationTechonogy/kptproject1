import axios from "axios";

export async function getAccessToken() {
const token = localStorage.getItem("access_token")
if (!token) return null

try {
    const res = await axios.get("http://localhost:8000/auth/verify", {
    headers: { Authorization: `Bearer ${token}` }
    })
    return token
} catch (e) {
    return null
}
}
