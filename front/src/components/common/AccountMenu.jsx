import { Link } from "react-router-dom";
import styled from "styled-components";
import Avatar from "./Avatar";

function AccountMenu() {
  // 로그인 비로그인 나눠야 함!
  return (
    <div>
      <AccountBox>
        <Link to="/login" style={{ textDecoration: "none" }}>
          로그인
        </Link>
        <Link to="/signup" style={{ textDecoration: "none" }}>
          회원가입
        </Link>
      </AccountBox>
      <Avatar />
    </div>
  );
}

const AccountBox = styled.div`
  display: flex;
  gap: 20px;
`;

export default AccountMenu;
