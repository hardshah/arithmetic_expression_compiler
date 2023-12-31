from llvmlite import ir, binding

MODULE_NAME = "test"

#LLVM

binding.initialize()
binding.initialize_native_target()
binding.initialize_all_asmprinters()

##Creating Module

module = ir.Module(name = MODULE_NAME)
builder = ir.IRBuilder()