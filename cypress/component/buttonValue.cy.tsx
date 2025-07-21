import Button from "../../src/components/Button";
import React from "react";

describe("buttonValue.cy.tsx", () => {
  it("stepper should default to 0", () => {
    cy.mount(<Button />);

    cy.get('span[id="count"]').should("have.text", "0");
  });
});
