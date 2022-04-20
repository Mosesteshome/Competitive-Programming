import logo from "./logo.svg";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Component from "./Component";
import Sidebar from "./Sidebar";
import { Row, Col, Container } from "react-bootstrap";

function App() {
    return (
        <Container fluid>
            <Row>
                <Col xs="auto" className="ps-0">
                    <Sidebar />
                </Col>
                <Col>
                    <Component />
                </Col>
            </Row>
        </Container>
    );
}

export default App;
