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

function Component() {
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
    <Container fluid className="">
      <Navbar expand="lg" bg="dark" variant="dark" fixed="top">
        <Container>
          <Navbar.Brand href="#home">
            <img
              alt=""
              src={logo}
              width="30"
              height="30"
              className="d-inline-block align-top"
            />{" "}
            Get funded Ethiopia
          </Navbar.Brand>
          <Form className="d-flex">
            <FormControl
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>

            <img alt="" src={logo} width="30" height="30" className="ms-4" />
          </Form>
        </Container>
      </Navbar>

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

export default Component;
