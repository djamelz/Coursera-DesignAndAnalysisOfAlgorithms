using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace SccComputation
{
    public class Main
    {
        public int[] ComputeScc(string filePath)
        {
            Dictionary<string, DfsItem> graph = new Dictionary<string, DfsItem>();
            Dictionary<string, DfsItem> graphRev = new Dictionary<string, DfsItem>();
            string[] values;
            DfsItem dfsItem;
            Stack<int> sccSize = new Stack<int>();

            using (StreamReader sr = new StreamReader(filePath))
            {
                while (sr.Peek() >= 0)
                {
                    values = sr.ReadLine().Split(' ');
                    if (graph.TryGetValue(values[0], out dfsItem))
                        dfsItem.AddEdge(values[1]);
                    else
                        graph.Add(values[0], new DfsItem(values[0], values[1]));

                    if (graphRev.TryGetValue(values[1], out dfsItem))
                        dfsItem.AddEdge(values[0]);
                    else
                        graphRev.Add(values[1],new DfsItem(values[1], values[0]));
                }
            }

            DfsLoop(graph, graphRev, sccSize);
            int[] a = sccSize.Where(x => x > 0).OrderByDescending(x => x).Take(5).ToArray();
            
            Array.Resize<int>(ref a, 5);
            
            //backtesting
            //sccSize = new Stack<int>();
            //DfsLoop(graphRev, graph, sccSize);
            //int[] b = sccSize.Where(x => x > 0).OrderByDescending(x => x).Take(5).ToArray();
            //Array.Resize<int>(ref b, 5);
            
            return a;
        }

        private void DfsLoop(Dictionary<string, DfsItem> graph, Dictionary<string, DfsItem> graphRev, Stack<int> sccSize)
        {
            Stack<string> order = new Stack<string>();
            Stack<string> sccMember;
            Stack<int> fakeS = new Stack<int>();
            DfsItem dfsItem;
            HashSet<string> visited = new HashSet<string>();

            foreach (var node in graphRev)
            {
                if ( !visited.Contains(node.Key) )
                {
                    DfsStack(graphRev, node.Value, order, 0, visited);
                }
            }

            visited = new HashSet<string>();
            foreach (var node in order)
            {

                if (graph.TryGetValue(node, out dfsItem))
                {
                    sccMember = new Stack<string>();
                    if (!visited.Contains(node))
                    {
                        sccSize.Push(DfsStack(graph, dfsItem, sccMember, 0, visited));
                    }
                }
                else
                {
                    visited.Add(node);
                    sccSize.Push(1);
                }
            }
            return;
        }

        private int DfsStack(Dictionary<string, DfsItem> graph, DfsItem currentDfsItem, Stack<string> order, int size, HashSet<string> visited)
        {
            Stack<DfsItem> stack = new Stack<DfsItem>();
            string addToStack;
            DfsItem dfsItem;

            stack.Push(currentDfsItem);
            while (stack.Count > 0)
            {
                addToStack = null;
                dfsItem = null;

                currentDfsItem = stack.Pop();
                visited.Add(currentDfsItem.Key);
                foreach (var edge in currentDfsItem.GetEdges())
                {
                    if(!visited.Contains(edge))
                    {
                        addToStack = edge;
                        break;     
                    }   
                }
                if (!string.IsNullOrEmpty(addToStack))
                {
                    stack.Push(currentDfsItem);
                    if (graph.TryGetValue(addToStack, out dfsItem))
                    {
                        stack.Push(dfsItem);
                    }
                    else
                    {
                        visited.Add(addToStack);
                        size++;
                        order.Push(addToStack);
                    }
                }
                else
                {
                    size++;
                    order.Push(currentDfsItem.Key);
                }
            }
            return size;
        }

        class DfsItem
        {
            public string Key { get; private set; }

            HashSet<string> _edges;
            
            public DfsItem(string key, string edge)
            {
                this.Key = key;
                _edges = new HashSet<string> { edge };
            }

            public void AddEdge(String node)
            {
                if(!_edges.Contains(node))
                    _edges.Add(node);
            }

            public HashSet<string> GetEdges()
            {
                return _edges;
            }
        }
    }
}
