using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SccComputation;

namespace UnitTests
{
    
    [TestClass]
    public class TestSccComputation
    {

        [TestMethod]
        public void TestComputeScc_test_file()
        {
            Main target = new Main();
            var result = target.ComputeScc(@".\..\..\..\UnitTests\test.txt");

            AssertArray(new int[] { 4, 3, 3, 1, 0 }, result);
        }

        [TestMethod]
        public void TestComputeScc_test7_file()
        {
            Main target = new Main();
            var result = target.ComputeScc(@".\..\..\..\UnitTests\test7.txt");

            AssertArray(new int[] { 36, 7, 1, 1, 1 }, result);
        }

        [TestMethod]
        public void TestComputeScc_test2_file()
        {
            Main target = new Main();
            var result = target.ComputeScc(@".\..\..\..\UnitTests\test2.txt");

            AssertArray(new int[] { 3, 3, 3, 0, 0 }, result);
        }

        [TestMethod]
        public void TestComputeScc_test3_file()
        {
            Main target = new Main();
            var result = target.ComputeScc(@".\..\..\..\UnitTests\test3.txt");

            AssertArray(new int[] { 1, 1, 1, 0, 0 }, result);
        }

        [TestMethod]
        public void TestComputeScc_real_file()
        {
            Main target = new Main();
            var result = target.ComputeScc(@".\..\..\..\UnitTests\SCC.txt");

            AssertArray(new int[] { 434821, 968, 459, 313, 211 }, result);
        }

        public void AssertArray(int[] expected, int[] actual)
        {
            Assert.AreEqual(expected.Count(), actual.Count());
            for (int i = 0; i < expected.Count(); i++)
            {
                Assert.AreEqual(expected[i], actual[i]);
            }
        }
    }
}
