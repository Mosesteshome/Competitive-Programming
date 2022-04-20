import {
  Col,
  Row,
  Card,
  Button,
  Container,
  Navbar,
  Form,
  FormControl,
} from "react-bootstrap";
import CardImage from "./logo192.png";
import logo from "./logo.png";
import "./App.css";

function Header() {
  const colors = [
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
  ];
  return (
    <Container fluid className="ps-0 pe-0">
      <header fluid className="p-3 bg-dark text-white">
        <div className="ps-0">
          <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start text-white">
            <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0 text-white">
              <Navbar.Brand href="#home">
                <img
                  alt=""
                  src={logo}
                  width="30"
                  height="30"
                  className="d-inline-block align-top"
                />{" "}
              </Navbar.Brand>
              <p className="text-secondary  text-justify   ">
                {" "}
                Get funded Ethiopia
              </p>
            </ul>

            <form className="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
              <FormControl
                type="search"
                className="form-control form-control-dark"
                placeholder="Search..."
                aria-label="Search"
              />
            </form>

            <div className="text-end">
              <Button type="Button" className="btn btn-outline-light me-2">
                Login
              </Button>
              <Button type="Button" className="btn btn-warning">
                Sign-up
              </Button>
            </div>
          </div>
        </div>
      </header>

      <Row className="g-4" xs={1} md={2} xl={3}>
        {colors.map((color, index) => (
          <Col key={index}>
            <Card bg={color} text={color === "light" ? "dark" : "white"}>
              <Card.Img variant="top" src={CardImage} />
              <Card.Body>
                <Card.Title>Card Title</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up
                  the bulk of the card's content.
                </Card.Text>
                <Button variant="primary">Go somewhere</Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default Header;
