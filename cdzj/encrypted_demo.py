# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import base64
"""
----RSA 解密价格  listWaterPrice
package c
{
   import com.hurlant.crypto.rsa.RSAKey;
   import mx.utils.Base64Decoder;
   import flash.utils.ByteArray;

   public class R extends Object
   {

      private static var rsa:RSAKey = null;

      public function R()
      {
         super();
      }

      public static function decode(encodedB64:String) : String
      {
         var N:String = null;
         var E:String = null;
         var D:String = null;
         var P:String = null;
         var Q:String = null;
         var DMP1:String = null;
         var DMQ1:String = null;
         var IQMP:String = null;
         if(rsa == null)
         {
            N = "9c2e6c195b482f28453f2bdf36d8016fac9c7dfbbd9493c9abbee2eaef080b39a56e8d3aab6f7d50827041bd09624a658706c949668320a28c2cdf4310dccbfb7021002b6079854bf25a52fe99087a5d898236116d1db9f93c75237d6b56c6172859bce759ffce500c4f30c780c9b3dd5dfff42dafa367638b956c09a26335c1";
            E = "10001";
            D = "6cc28f18a14e85385ff07bd6b75478bb91d270910c16194c894326b63fbab4467283a7e9c154a4499a6c1dfb4c3b9c5f53465089c2cf71bc802d0754a6bb7b78087c3a232ed165768d2898a900183a788d8a85eea130a079ece9b7d07839918ae46830f73108e27e85590f9ba69395d9d455f4b71012c327518250ad60b5d0f9";
            P = "d0fdd6eea2f6f3a8b25d66fb133d50413598b86a9a5f205cc97e02593a38d5c49602f7ab2495f46343aa8c694f8ae5067ad1965a0902e1497ab725841559ebbb";
            Q = "bf4fa989b201f1d6a970012cae0cfb478231c98753732acfdb500b82b87879a3199315f7f435b8739c7a351e7dce61fcc8811384fb1522b418602a2f56a706b3";
            DMP1 = "28d7f3116037f3169d0534030d9785ffb881c848cd329a188828603d1febcb9b47d5fca12ddd408dc5c3a6fd4dd64f3c1cf4a8f59f9d387a2bc96f438908b1d1";
            DMQ1 = "a7bafd66a7360345746aa9ecf5709642dcc82febc0e3814e99f6f5109811b07baa2986224def67979d429c1deea92aca0934f9db2694224809f30e2950ecc1f7";
            IQMP = "8e37f816f3b08e1078fb267bb16171cc3ea93d8be87f9fdd9b7b2b1779430e9ac8fb71f326550f7df79c5ba85136546f034b5cbe39784f209b328f262797c50d";
            rsa = RSAKey.parsePrivateKey(N,E,D,P,Q,DMP1,DMQ1,IQMP);
         }
         var base64de:Base64Decoder = new Base64Decoder();
         base64de.decode(encodedB64);
         var src:ByteArray = base64de.toByteArray();
         var dst2:ByteArray = new ByteArray();
         rsa.decrypt(src,dst2,src.length);
         return dst2.toString();
      }
   }
}


"""

"""
--- base64 编码
package mx.utils
{
   import flash.utils.ByteArray;
   import mx.resources.IResourceManager;
   import mx.resources.ResourceManager;

   [ResourceBundle("utils")]
   public class Base64Decoder extends Object
   {

      private static const ESCAPE_CHAR_CODE:Number = 61;

      private static const inverse:Array = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,62,64,64,64,63,52,53,54,55,56,57,58,59,60,61,64,64,64,64,64,64,64,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,64,64,64,64,64,64,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64];

      private var count:int = 0;

      private var data:ByteArray;

      private var filled:int = 0;

      private var work:Array;

      private var resourceManager:IResourceManager;

      public function Base64Decoder()
      {
         this.work = [0,0,0,0];
         this.resourceManager = ResourceManager.getInstance();
         super();
         this.data = new ByteArray();
      }

      public function decode(encoded:String) : void
      {
         var c:* = NaN;
         for(var i:uint = 0; i < encoded.length; i++)
         {
            c = encoded.charCodeAt(i);
            if(c == ESCAPE_CHAR_CODE)    # ESCAPE_CHAR_CODE = 61
            {
               this.work[this.count++] = -1;
               if(this.count == 4)
               {
                  this.count = 0;
                  this.data.writeByte(this.work[0] << 2 | (this.work[1] & 255) >> 4);
                  this.filled++;
                  if(this.work[2] == -1)
                  {
                     break;
                  }
                  this.data.writeByte(this.work[1] << 4 | (this.work[2] & 255) >> 2);
                  this.filled++;
                  if(this.work[3] == -1)
                  {
                     break;
                  }
                  this.data.writeByte(this.work[2] << 6 | this.work[3]);
                  this.filled++;
               }
            }
            else if(inverse[c] != 64)
            {
               this.work[this.count++] = inverse[c];
            }
         }
      }

      public function drain() : ByteArray
      {
         var result:ByteArray = new ByteArray();
         var oldPosition:uint = this.data.position;
         this.data.position = 0;
         result.writeBytes(this.data,0,this.data.length);
         this.data.position = oldPosition;
         result.position = 0;
         this.filled = 0;
         return result;
      }

      public function flush() : ByteArray
      {
         var message:String = null;
         if(this.count > 0)
         {
            message = this.resourceManager.getString("utils","partialBlockDropped",[this.count]);
            throw new Error(message);
         }
         return this.drain();
      }

      public function reset() : void
      {
         this.data = new ByteArray();
         this.count = 0;
         this.filled = 0;
      }

      public function toByteArray() : ByteArray
      {
         var result:ByteArray = this.flush();
         this.reset();
         return result;
      }
   }
}



"""


class Base64Decoder(object):
    ESCAPE_CHAR_CODE = 61
    inverse = [64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 64, 64, 63, 52, 53, 54, 55,
               56, 57, 58, 59, 60, 61, 64, 64, 64, 64, 64, 64, 64, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 64, 64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
               36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
               64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64]
    count = 0
    data = bytearray()
    filled = 0
    work = [0, 0, 0, 0]
    resourceManager = ''  # todo

    def decode(self, string):
        for s in string:
            c = ord(s)
            if c == self.ESCAPE_CHAR_CODE:
                self.count += 1
                self.work[self.count] = -1
                if self.count == 4:
                    self.count = 0
                    self.data += (self.work[0] << 2 | (self.work[1] & 255) >> 4)
                    self.filled += 1
                    if self.work[2] == -1:
                        break
                    self.data += (self.work[1] << 4 | (self.work[2] & 255) >> 2)
                    self.filled += 1
                    if self.work[3] == -1:
                        break
                    self.data += (self.work[2] << 6 | self.work[3])
                    self.filled += 1
            elif self.inverse[c] != 64:
                self.count += 1
                self.work[self.count] = self.inverse[c]
        print(self.data)

    def drain(self):
        result = bytearray == b''


if __name__ == '__main__':
    c = Base64Decoder()
    c.decode("""Bu+xc15Le4JDkTKtCLhcLsvdquePi7HIiwKnBwCOCF8xW8/ZO3WksL1Fjk0lMEgt8AVmI+0XapnQQ92EGxXJ4iG1GMqTS8TxcadZO6fvzNE9AC3wkD5kNsisC1zGpVldNA3/X4OQOL8Ut9o+B44v1GfM9MBuIE0BgwHf23hZgM0=
    """)
