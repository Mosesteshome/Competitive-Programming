import { Button } from "react-bootstrap";
import "./sidebar.css";

function SideBar() {
  var bootstrap;
  (function () {
    "use strict";
    var tooltipTriggerList = [].slice.call(
      document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl);
    });
  })();
  return (
    <div className="flex-shrink-0 p-3 bg-white">
      <a
        href="/"
        className="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom"
      >
        <span className="fs-5 fw-semibold">Collapsible</span>
      </a>
      <ul className="list-unstyled ps-0">
        <li className="mb-1">
          <Button
            className="btn btn-toggle align-items-center rounded collapsed"
            data-bs-toggle="collapse"
            data-bs-target="#home-collapse"
            aria-expanded="true"
          >
            Home
          </Button>
          <div className="collapse show" id="home-collapse">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li>
                <a href="#" className="link-dark rounded">
                  Overvie
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Updates
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Reports
                </a>
              </li>
            </ul>
          </div>
        </li>
        <li className="mb-1">
          <Button
            className="btn btn-toggle align-items-center rounded collapsed"
            data-bs-toggle="collapse"
            data-bs-target="#dashboard-collapse"
            aria-expanded="false"
          >
            Dashboard
          </Button>
          <div className="collapse" id="dashboard-collapse">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li>
                <a href="#" className="link-dark rounded">
                  Overview
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Weekly
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Monthly
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Annually
                </a>
              </li>
            </ul>
          </div>
        </li>
        <li className="mb-1">
          <Button
            className="btn btn-toggle align-items-center rounded collapsed"
            data-bs-toggle="collapse"
            data-bs-target="#orders-collapse"
            aria-expanded="false"
          >
            Orders
          </Button>
          <div className="collapse" id="orders-collapse">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li>
                <a href="#" className="link-dark rounded">
                  New
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Processed
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Shipped
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Returned
                </a>
              </li>
            </ul>
          </div>
        </li>
        <li className="border-top my-3"></li>
        <li className="mb-1">
          <Button
            className="btn btn-toggle align-items-center rounded collapsed"
            data-bs-toggle="collapse"
            data-bs-target="#account-collapse"
            aria-expanded="false"
          >
            Account
          </Button>
          <div className="collapse" id="account-collapse">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li>
                <a href="#" className="link-dark rounded">
                  New...
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Profile
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Settings
                </a>
              </li>
              <li>
                <a href="#" className="link-dark rounded">
                  Sign out
                </a>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  );
}
export default SideBar;
