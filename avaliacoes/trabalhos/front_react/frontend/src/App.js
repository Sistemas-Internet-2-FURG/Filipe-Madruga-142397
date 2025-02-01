import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate, Link } from "react-router-dom";
import axios from "axios";

const API_URL = "http://localhost:5000";

function Home() {
  return (
    <div>
      <button><Link to="/login">Login</Link></button>
      <button><Link to="/register">Register</Link></button>
    </div>
  );
}

function Login({ setToken }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/auth/login`, { useremail: email, userpassw: password });
      const token = response.data.token;
      setToken(token);
      localStorage.setItem('token', token);
      navigate("/crud");
    } catch (err) {
      setError(err.response?.data.message || "Login failed");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} method="post">
        <h2>Sign in</h2>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <label htmlFor="useremail">E-mail</label>
        <input type="text" name="useremail" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <label htmlFor="password">Password</label>
        <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit">Enter</button>
        <p>Do not have an account? <Link to="/register">Sign up</Link></p>
      </form>
    </div>
  );
}

function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [confirmEmail, setConfirmEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_URL}/auth/register`, {
        username,
        useremail: email,
        userconfirmemail: confirmEmail,
        userpassw: password,
        userconfirmpassw: confirmPassword,
      });
      alert("User registered successfully");
      navigate("/login");
    } catch (err) {
      setError(err.response?.data.message || "Registration failed");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} method="post">
        <h2>Sign up</h2>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <label htmlFor="username">Username</label>
        <input type="text" name="username" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <label htmlFor="useremail">E-mail</label>
        <input type="text" name="useremail" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <label htmlFor="userconfirmemail">Confirm your E-mail</label>
        <input type="text" name="userconfirmemail" placeholder="E-mail" value={confirmEmail} onChange={(e) => setConfirmEmail(e.target.value)} required />
        <label htmlFor="password">Password</label>
        <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <label htmlFor="confirm_password">Confirm your password</label>
        <input type="password" name="confirm_password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required />
        <button type="submit">Sign up</button>
        <p>Already have an account? <Link to="/login">Sign in</Link></p>
      </form>
    </div>
  );
}

function RegisterStudent() {
  const [registration, setRegistration] = useState('');
  const [studentname, setStudentname] = useState('');
  const [classcode, setClasscode] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/crud/register/student`, {
        registration, studentname, classcode
      }, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      setMessage(response.data.message);
      setError('');
      window.location.reload();
    } catch (err) {
      setError(err.response?.data.message || 'Registration failed');
      setMessage('');
    }
  };

  return (
    <div>
      <h3>Register Student</h3>
      <form onSubmit={handleRegister}>
        <input type="text" placeholder="Registration" value={registration} onChange={(e) => setRegistration(e.target.value)} required />
        <input type="text" placeholder="Student Name" value={studentname} onChange={(e) => setStudentname(e.target.value)} required />
        <input type="text" placeholder="Class Code" value={classcode} onChange={(e) => setClasscode(e.target.value)} required />
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
    </div>
  );
}

function RemoveClass() {
  const [classcode, setClasscode] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleRemove = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/crud/remove/class`, {
        classcode
      }, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      setMessage(response.data.message);
      setError('');
      window.location.reload();
    } catch (err) {
      setError(err.response?.data.message || 'Removal failed');
      setMessage('');
    }
  };

  return (
    <div>
      <h3>Remove Class</h3>
      <form onSubmit={handleRemove}>
        <input type="text" placeholder="Class Code" value={classcode} onChange={(e) => setClasscode(e.target.value)} required />
        <button type="submit">Remove</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
    </div>
  );
}

function UpdateStudent() {
  const [registration, setRegistration] = useState('');
  const [classcode, setClasscode] = useState('');
  const [action, setAction] = useState('insert');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleUpdate = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/crud/update/student`, {
        registration, classcode, action
      }, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      setMessage(response.data.message);
      setError('');
      window.location.reload();
    } catch (err) {
      setError(err.response?.data.message || 'Update failed');
      setMessage('');
    }
  };

  return (
    <div>
      <h3>Update Student</h3>
      <form onSubmit={handleUpdate}>
        <input type="text" placeholder="Registration" value={registration} onChange={(e) => setRegistration(e.target.value)} required />
        <input type="text" placeholder="Class Code" value={classcode} onChange={(e) => setClasscode(e.target.value)} required />
        <label htmlFor="action">Action</label>
        <select name="action" value={action} onChange={(e) => setAction(e.target.value)} required>
          <option value="insert">Insert</option>
          <option value="remove">Remove</option>
        </select>
        <button type="submit">Update</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
    </div>
  );
}

function RegisterClass() {
  const [classcode, setClasscode] = useState('');
  const [classname, setClassname] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/crud/register/class`, {
        classcode, classname
      }, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      setMessage(response.data.message);
      setError('');
      window.location.reload();
    } catch (err) {
      setError(err.response?.data.message || 'Registration failed');
      setMessage('');
    }
  };

  return (
    <div>
      <h3>Register Class</h3>
      <form onSubmit={handleRegister}>
        <input type="text" placeholder="Class Code" value={classcode} onChange={(e) => setClasscode(e.target.value)} required />
        <input type="text" placeholder="Class Name" value={classname} onChange={(e) => setClassname(e.target.value)} required />
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
    </div>
  );
}

function RemoveStudent() {
  const [registration, setRegistration] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleRemove = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/crud/remove/student`, {
        registration
      }, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      setMessage(response.data.message);
      setError('');
      window.location.reload();
    } catch (err) {
      setError(err.response?.data.message || 'Removal failed');
      setMessage('');
    }
  };

  return (
    <div>
      <h3>Remove Student</h3>
      <form onSubmit={handleRemove}>
        <input type="text" placeholder="Registration" value={registration} onChange={(e) => setRegistration(e.target.value)} required />
        <button type="submit">Remove</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>{error}</p>}
    </div>
  );
}


function Crud() {
  const [data, setData] = useState({ students: [], classes: [], classes_students: [] });
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${API_URL}/crud/`, {
          headers: { 'Authorization': localStorage.getItem('token') }
        });
        setData(response.data);
      } catch (err) {
        if (err.response && err.response.status === 401) {
          navigate('/login');
        }
      }
    };
    fetchData();
  }, [navigate]);
  return (
    <div>
      <h2>Crud View</h2>
      <h3>My Classes</h3>
      <table>
        <thead>
          <tr>
            <th>Class Code</th>
            <th>Class Name</th>
          </tr>
        </thead>
        <tbody>
          {data.classes.map((classe, index) => (
            <tr key={index}>
              <td>{classe[0]}</td>
              <td>{classe[1]}</td>
            </tr>
          ))}
        </tbody>
      </table>
      
      <h3>My Students</h3>
      <table>
        <thead>
          <tr>
            <th>Registration</th>
            <th>Student</th>
          </tr>
        </thead>
        <tbody>
          {data.students.map((student, index) => (
            <tr key={index}>
              <td>{student[0]}</td>
              <td>{student[1]}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <br />
      <br />

      <h3>My Classes and Students</h3>
      <table>
        <thead>
          <tr>
            <th>Class Code</th>
            <th>Registration</th>
          </tr>
        </thead>
        <tbody>
          {data.classes_students.map((cs, index) => (
            <tr key={index}>
              <td>{cs[0]}</td>
              <td>{cs[1]}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <RegisterClass  />
      <RemoveClass  />
      <RegisterStudent  />
      <UpdateStudent  />
      <RemoveStudent  />
    </div>
  );
}


function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);
    } else {
      localStorage.removeItem("token");
    }
  }, [token]);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/crud" element={<Crud />} />
      </Routes>
    </Router>
  );
}

export default App;