# LangGraph

Compared with LangChain, LangGraph offers a clear workflow, inspired by the graph, LangGraph composed by States, Nodes and Edges. Through this way, we can better see how the agent make decisions and take actions, that's why I move to LangGraph from LangChain (see my previous work on Perovskite Multi-AI agent)

## Graphs

1. [`State`](https://docs.langchain.com/oss/python/langgraph/graph-api#state): A shared data structure that represents the current snapshot of your application. It can be any data type, but is typically defined using a shared state schema.
2. [`Nodes`](https://docs.langchain.com/oss/python/langgraph/graph-api#nodes): Functions that encode the logic of your agents. They receive the current state as input, perform some computation or side-effect, and return an updated state.
3. [`Edges`](https://docs.langchain.com/oss/python/langgraph/graph-api#edges): Functions that determine which `Node` to execute next based on the current state. They can be conditional branches or fixed transitions.

Which means **nodes** do the work, while **Edges** tell what to do next.

## State

The first thing you do when you define a graph is define the `State` of the graph. The `State` consists of the [schema of the graph](https://docs.langchain.com/oss/python/langgraph/graph-api#schema) as well as [`reducer` functions](https://docs.langchain.com/oss/python/langgraph/graph-api#reducers) which specify how to apply updates to the state. The schema of the `State` will be the input schema to all `Nodes` and `Edges` in the graph, and can be either a `TypedDict` or a `Pydantic` model. All `Nodes` will emit updates to the `State` which are then applied using the specified `reducer` function.

### Schema

The main documented way to specify the schema of a graph is by using a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict). If you want to provide default values in your state, use a [`dataclass`](https://docs.python.org/3/library/dataclasses.html). We also support using a Pydantic [BaseModel](https://docs.langchain.com/oss/python/langgraph/graph-api.md#use-pydantic-models-for-graph-state) as your graph state if you want recursive data validation (though note that pydantic is less performant than a `TypedDict` or `dataclass`).By default, the graph will have the same input and output schemas. If you want to change this, you can also specify explicit input and output schemas directly. This is useful when you have a lot of keys, and some are explicitly for input and others for output. See the [guide here](https://docs.langchain.com/oss/python/langgraph/graph-api.md#define-input-and-output-schemas) for how to use.