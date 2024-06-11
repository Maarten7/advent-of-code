class FundamentalElement {
  readonly _type: "fire" | "water" | "earth" | "air";

  public constructor(tiepe: "fire" | "water" | "earth" | "air") {
    this._type = tiepe;
  }
}

class Avatar {
  private _name: string;

  public constructor(name: string) {
    this._name = name;
  }

  public combine(element1: FundamentalElement, element2: FundamentalElement) {
    let alchemy: Alchemy = new Alchemy(element1, element2);
    return alchemy;
  }
}

class Alchemy {
  private _type: string;
  private _element1: FundamentalElement;
  private _element2: FundamentalElement;

  public constructor(
    element1: FundamentalElement,
    element2: FundamentalElement
  ) {}
}
