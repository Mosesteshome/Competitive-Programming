import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Layout from "./layout";
import Header from "./header";
import SideBar from "./sidebar";
import { Row, Col, Container } from "react-bootstrap";

function App() {
  return (
    <Container fluid>
      <Row>
        <Col xs="auto" className="ps-0">
          <SideBar />
        </Col>
        <Col>
          <Header />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
