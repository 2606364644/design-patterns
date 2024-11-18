from abc import ABC, abstractmethod


# 先写业务
class ProductBase(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(ProductBase):
    # def operation1(self) -> str:
    #     return "{Result of the ConcreteProduct1}"
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

# 再写工厂
class Creator(ABC):
    _object_map = {
        "ConcreteProduct1": ConcreteProduct1
    }

    @abstractmethod
    def factory_method(self) -> None:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

    @staticmethod
    def create_object(type_: str):
        return Creator._object_map[type_]()

class ConcreteCreator1(Creator):
    def factory_method(self) -> ProductBase:
        return ConcreteProduct1()


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    # client_code(ConcreteCreator1())
    product1 = Creator.create_object("ConcreteProduct1")
    print(product1.operation())
