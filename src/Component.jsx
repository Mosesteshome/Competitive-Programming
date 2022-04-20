import { Col, Row, Card, Button, Container } from "react-bootstrap";
import CardImage from "./logo192.png";

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
