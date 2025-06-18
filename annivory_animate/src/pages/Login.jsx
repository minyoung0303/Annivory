import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // CSRF 토큰 필요 시 여기에 추가
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            window.location.href = '/';
        } else {
            setError('아이디 혹은 비밀번호를 잘못 입력하였습니다.');
        // 아이디 O , 비밀번호 틀렸다고 문구
        // 아이디 X , 아이디 틀렸다고 문구
        // 없는 정보 : 존재하지 않는 정보입니다.
        }
    };

    const handleSignupRedirect = () => {
        navigate('/signup');
    };

    return (
        <div style={{ padding: 40 }}>
            <h2>로그인 페이지</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>아이디</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>비밀번호</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">로그인</button>
                <button type="button" onClick={{handleSignupRedirect}}>회원가입</button>
            </form>
        </div>
    );
}

export default Login;